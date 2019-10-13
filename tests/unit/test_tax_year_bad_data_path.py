import os
import unittest

from income_tax_calculator.tax_year import TaxYear, DataFileNotFoundException


class TestTaxYearBadDataPath(unittest.TestCase):
    _non_existent_test_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                '../fixtures/does-not-exist-data.json')

    def test_data_file_does_not_exist(self):
        with self.assertRaises(DataFileNotFoundException):
            TaxYear.set_data_file(TestTaxYearBadDataPath._non_existent_test_data_path)


if __name__ == '__main__':
    unittest.main()
