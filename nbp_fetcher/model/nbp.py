import json

import requests
from bs4 import BeautifulSoup


class FetchWeb:

    def __init__(self, link: str):
        self.link = link
        self.data_page = []
        self.date_release = None
        self.currencies = []

    def load_data(self):
        self._fetch_page()
        self._get_effective_date()
        self._get_all_data()

    def _fetch_page(self):
        response = requests.get(self.link)
        data = BeautifulSoup(response.content, 'html.parser').text
        self.data_page = json.loads(data)[0]


    def _get_effective_date(self):
        self.date_release = self.data_page['effectiveDate']

    def _get_all_data(self):
        self.currencies = self.data_page['rates']
