import bs4

from bot.parsers.parser import Parser


class LentaParser(Parser):

    def __init__(self):
        super().__init__()
        self.HOST = 'https://lenta.ru/'
        self.HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/91.0.4472.101 Safari/537.36', 'accept': '*/*'}

        self.URL = 'https://lenta.ru/rubrics/world/'

        self.urls = {
            'World': 'https://lenta.ru/rubrics/world/',
            'Economic': 'https://lenta.ru/rubrics/economics/',
            'Culture': 'https://lenta.ru/rubrics/culture/',
            'Science': 'https://lenta.ru/rubrics/science/',
            'Sport': 'https://lenta.ru/rubrics/sport/',
            'Internet': 'https://lenta.ru/rubrics/media/',
            'Life': 'https://lenta.ru/rubrics/life/',
            'Russian': 'https://lenta.ru/rubrics/russia/',
            'Crime': 'https://lenta.ru/rubrics/forces/'
        }

    def parse(self, key=None) -> list:

        html = self.get_html()
        content = self.get_content(html.text, 'div', "b-tabloid__topic_news")

        link_list = list()

        for item in content:

            val = item.find('span', class_='g-date item__date')

            if type(val) == bs4.element.Tag:

                if val.get_text().find("Сегодня") != -1:
                    link_list.append(self.HOST + item.find('a').get('href'))

        return link_list
