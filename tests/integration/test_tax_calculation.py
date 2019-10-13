import os
import unittest

from income_tax_calculator.tax_year import TaxYear


class TestTaxCalcuation(unittest.TestCase):
    _simple_test_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../fixtures/simple-data.json')

    @classmethod
    def setUpClass(cls) -> None:
        TaxYear.set_data_file(cls._simple_test_data_path)

    # Test zero tax due when gross income below personal allowance
    def test_tax_calculation_below_personal_allowance_1(self):
        t = TaxYear(2017)
        self.assertEqual(0, t.get_total_tax_due(gross_income=11499))

    def test_tax_calculation_below_personal_allowance_2(self):
        t = TaxYear(2018)
        self.assertEqual(0, t.get_total_tax_due(11849))

    # Test tax due when into first band
    def test_tax_calculation_first_rate_band_1(self):
        t = TaxYear(2017)
        self.assertEqual(0.20, t.get_total_tax_due(gross_income=11501))

    def test_tax_calculation_first_rate_band_2(self):
        t = TaxYear(2018)
        self.assertEqual(0.19, t.get_total_tax_due(gross_income=11851))

    # Test tax due when into second band (but not the top band)
    def test_tax_calculation_second_rate_band_1(self):
        t = TaxYear(2018)
        self.assertEqual(14150, t.get_taxable_income(gross_income=26000))
        self.assertEqual(2829.59, t.get_total_tax_due(gross_income=26000))


if __name__ == '__main__':
    unittest.main()
