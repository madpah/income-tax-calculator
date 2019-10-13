import json
import os

from income_tax_calculator.tax_rate import TaxRate

TAX_YEAR_DATA_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/rates.json')


class TaxYear:
    _key = None
    _name = None
    _personal_allowance = None
    _rates = []

    @staticmethod
    def _load_tax_year_data(year_key):
        try:
            with open(TAX_YEAR_DATA_FILE, 'r') as data_file:
                rate_data = json.load(data_file)

                if str(year_key) in list(rate_data.keys()):
                    return rate_data[str(year_key)]
                else:
                    raise Exception("No rate data available for Tax Year {}. "
                                    "Available years are: {}".format(year_key, list(rate_data.keys())))

        except Exception as e:
            print("Exception: {}".format(str(e)))

    def __init__(self, year_key=None):
        if year_key is None:
            raise Exception("No Tax Year key supplied!")

        self._key = year_key
        tax_year_data = TaxYear._load_tax_year_data(self._key)
        self._name = tax_year_data['name']
        self._personal_allowance = tax_year_data['personal_allowance']
        for rate in tax_year_data['rates']:
            self._rates.append(TaxRate(**rate))

    def get_tax_rates(self):
        return self._rates
