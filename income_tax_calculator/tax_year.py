import json
import os

from income_tax_calculator.tax_rate import TaxRate


def format_financial_figure(val):
    """

    :type val: int
    """
    return "£{:,.2f}".format(val)


class TaxYear:
    tax_year_data_file: str = None

    _key: int = None
    _name: str = None
    _personal_allowance: int = None
    _rates: list = []

    @staticmethod
    def set_data_file(data_file_path):
        # Test file exists
        if not os.path.exists(data_file_path):
            raise DataFileNotFoundException

        # Set the static class variable
        TaxYear.tax_year_data_file = data_file_path

    @staticmethod
    def load_tax_year_data(year_key: int) -> dict:
        """
        Attempts to load Tax Year rate bands from the source data for the specified
        year.

        :param year_key: int
        :return: dict
        """
        # If the data file is None, it means TaxYear.set_data_file has yet to be called
        if TaxYear.tax_year_data_file is None:
            raise DataFileNotSpecifiedException

        # Open the data file and attempt to get the requested years' configuration
        with open(TaxYear.tax_year_data_file, 'r') as data_file:
            rate_data = json.load(data_file)

            if str(year_key) in list(rate_data.keys()):
                return rate_data[str(year_key)]
            else:
                raise UnknownTaxYearException("No rate data available for Tax Year {}. "
                                              "Available years are: {}".format(year_key, list(rate_data.keys())))

    def __init__(self, year_key: int = None) -> object:
        """
        Constructor

        :param year_key: int
        """
        if year_key is None:
            raise NoTaxYearSuppliedException

        self._key = year_key
        tax_year_data = TaxYear.load_tax_year_data(self._key)
        self._name = tax_year_data['name']
        self._personal_allowance = tax_year_data['personal_allowance']
        self._rates = []
        for rate in tax_year_data['rates']:
            self._rates.append(TaxRate(**rate))

    def get_name(self) -> str:
        return self._name

    def get_personal_allowance(self):
        return self._personal_allowance

    def get_tax_rates(self) -> list:
        return self._rates

    def get_taxable_income(self, gross_income) -> int:
        if gross_income > self.get_personal_allowance():
            return gross_income - self.get_personal_allowance()
        else:
            return 0

    def get_total_tax_due(self, gross_income):
        total_tax_due = 0.00
        taxable_income = self.get_taxable_income(gross_income=gross_income)
        for tax_rate in self.get_tax_rates():
            total_tax_due += TaxRate.get_tax_due_for_tax_rate(taxable_income=taxable_income, tax_rate=tax_rate)
        return total_tax_due

    def print_calculation(self, gross_income: int):
        print("Tax Year: {}".format(self.get_name()))
        print("")
        print("Gross Salary: {}".format(format_financial_figure(gross_income)))
        print("")
        print("Personal Allowance: {}".format(format_financial_figure(self.get_personal_allowance())))
        print("")
        print("Taxable Income: {}".format(format_financial_figure(self.get_taxable_income(gross_income))))
        print("")
        taxable_income = self.get_taxable_income(gross_income=gross_income)
        for tax_rate in self.get_tax_rates():
            tax_rate_tax_due = TaxRate.get_tax_due_for_tax_rate(taxable_income=taxable_income, tax_rate=tax_rate)
            print("{}: {} @{}% = {}".format(tax_rate.get_name(), format_financial_figure(
                tax_rate.get_taxable_amount(taxable_income=taxable_income)), tax_rate.get_percentage(),
                                            format_financial_figure(tax_rate_tax_due)))

        print("")
        print("Total Tax Due: {}".format(format_financial_figure(self.get_total_tax_due(gross_income=gross_income))))


class DataFileNotFoundException(Exception):
    pass


class DataFileNotSpecifiedException(Exception):
    pass


class NoTaxYearSuppliedException(Exception):
    pass


class UnknownTaxYearException(Exception):
    pass
