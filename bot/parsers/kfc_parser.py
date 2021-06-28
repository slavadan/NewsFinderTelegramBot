from bot.parsers.parser import *


class KfcParser(Parser):

    def __init__(self):
        super().__init__()
        self.URL = 'https://www.kfc.by/'
        self.HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/91.0.4472.101 Safari/537.36', 'accept': '*/*'}

    def parse(self, key=None):
        html = self.get_html()
        content = self.get_content(html.text, 'h2', "product-lnk")

        link_list = list()

        for item in content:
            link_list.append(item.find('a').get('href'))

        return link_list
