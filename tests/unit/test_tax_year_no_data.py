import unittest

from income_tax_calculator.tax_year import TaxYear, DataFileNotSpecifiedException


class TestTaxYearNoData(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        TaxYear.tax_year_data_file = None

    def test_no_data_file_specified(self):
        with self.assertRaises(DataFileNotSpecifiedException):
            TaxYear.load_tax_year_data(2016)


if __name__ == '__main__':
    unittest.main()
