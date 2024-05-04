from nbp_fetcher.model.nbp import FetchWeb


class DataWeb:

    def __init__(self, link: str = 'http://api.nbp.pl/api/exchangerates/tables/A/'):
        self.fetch_web = FetchWeb(link)
        self.fetch_web.load_data()
        self.lst_currencies = []
        self.dct_currencies = {}

    def load_data(self):
        self._get_currencies()
        self._data()

    def _get_currencies(self):
        self.lst_currencies = [currencies['code'] for currencies in
                               self.fetch_web.currencies]

    def _data(self):
        self.dct_currencies = {currencies['code']: currencies['mid']
                               for currencies in self.fetch_web.currencies}
