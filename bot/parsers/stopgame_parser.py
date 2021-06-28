from bot.parsers.parser import *



class StopGameParser(Parser):

    def __init__(self):

        super().__init__()

        self.URL = 'https://stopgame.ru/news'
        self.HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/91.0.4472.101 Safari/537.36', 'accept': '*/*'}

        self.HOST = 'https://stopgame.ru/'

        self.urls = {
            'All': 'https://stopgame.ru/news',
            'PC': 'https://stopgame.ru/news/pc',
            'XboxOne': 'https://stopgame.ru/news/xone',
            'XboxX': 'https://stopgame.ru/news/xboxsx',
            'PS4': 'https://stopgame.ru/news/ps4',
            'PS5': 'https://stopgame.ru/news/ps5',
            'MMO': 'https://stopgame.ru/news/mmo',
            'CyberSport': 'https://stopgame.ru/news/cybersport',
            'Films': 'https://stopgame.ru/news/movies'
        }

    def parse(self, key=None):

        html = self.get_html()
        content = self.get_content(html.text, 'div', "article-description")

        link_list = list()

        for item in content:
            if item.find('span', class_="info-item timestamp").get_text() == "Сегодня":
                link_list.append(self.HOST + item.find('a').get('href'))

        return link_list
