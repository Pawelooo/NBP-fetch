from nbp_fetcher.view.view import View

from nbp_fetcher.model.model import DataWeb


class Controller:

    def __init__(self):
        self.view = View()
        self.model = DataWeb()

    def controller(self):
        while True:
            self.view.print_message(
                'What you want to do:\n 1. Converts PLN to currency\n 2. Converts currency into PLN\n 3. Exit')
            res = self.view.get_value('Your choice :')
            try:
                res = int(res)
            except ValueError as e:
                self.view.print_message('You entered the wrong value format : '
                                        + str(e))
            else:
                self._check_currencies(res)
            self.view.print_message('')

    def _currencies_list(self):
        self.view.print_message('*' * 80)
        self.view.print_message(
            '*' + f'Actual currencies available from {self.model.fetch_web.date_release}'.center(
                78) + '*')
        self.view.print_message('*' * 80)
        value = 40
        for idx, currencies in enumerate(self.model.fetch_web.currencies):
            if idx >= 9:
                value = 39
            self.view.print_message(
                f'{idx + 1}. {currencies["currency"].ljust(value).capitalize()}  {currencies["code"]}: {currencies["mid"]} PLN')

    def _check_currencies(self, option: int):
        result = None
        cur = 'PLN'
        if option == 3:
            return None
        if option in (1, 2):
            self._currencies_list()
            self.model.load_data()
            currency = self.view.get_value(
                'What currency (enter the abbreviation) :')
            if currency in self.model.lst_currencies:
                val = self.model.dct_currencies[currency]
                value = self.view.get_value(
                    'How much money he wants to change :')
                if option == 1:
                    result = round(float(value) / val, 2)
                    cur = currency
                if option == 2:
                    result = round(val * float(value), 2)
                self.view.print_message(
                    f'After the exchange You would have this much: {result} {cur}')
            else:
                self.view.print_message(
                    f'There is no such currency {currency}')
        else:
            self.view.print_message(
                f'There is no such option on this number {option}')
