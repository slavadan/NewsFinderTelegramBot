import requests
from bs4 import BeautifulSoup
import abc


class Parser(abc.ABC):

    def __init__(self):
        self.URL = ''
        self.HOST = ''
        self.HEADERS = {}
        self.urls = {}

    @abc.abstractmethod
    def parse(self, key=None):
        pass

    def get_html(self, params=None):
        return requests.get(self.URL, headers=self.HEADERS, params=params)

    def set_category(self, key):
        self.URL = self.urls.get(key)

    def get_content(self, html, tag, info):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all(tag, class_=info)

        return items
