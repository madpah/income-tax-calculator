import os
import unittest

from income_tax_calculator.tax_year import TaxYear, NoTaxYearSuppliedException, UnknownTaxYearException


class TestTaxYear(unittest.TestCase):
    _simple_test_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../fixtures/simple-data.json')

    @classmethod
    def setUpClass(cls) -> None:
        TaxYear.set_data_file(cls._simple_test_data_path)

    def test_load_tax_year_non_existent(self):
        with self.assertRaises(UnknownTaxYearException):
            TaxYear.load_tax_year_data(2016)

    def test_load_tax_year_exists(self):
        self.assertIsInstance(TaxYear.load_tax_year_data(2017), dict)

    def test_constructor_no_tax_year(self):
        with self.assertRaises(NoTaxYearSuppliedException):
            TaxYear(year_key=None)

    def test_constructor_known_tax_year(self):
        self.assertIsInstance(TaxYear(2017), TaxYear)


if __name__ == '__main__':
    unittest.main()
