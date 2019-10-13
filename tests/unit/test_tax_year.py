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

    def test_tax_year_name(self):
        t = TaxYear(2017)
        self.assertEqual('2017-2018', t.get_name())

    def test_tax_year_rates_1(self):
        t = TaxYear(2017)
        self.assertEqual(2, len(t.get_tax_rates()))

    def test_tax_year_rates_2(self):
        t = TaxYear(2018)
        self.assertEqual(5, len(t.get_tax_rates()))

    def test_personal_allowance_1(self):
        t = TaxYear(2017)
        self.assertEqual(11500.00, t.get_personal_allowance())

    def test_personal_allowance_2(self):
        t = TaxYear(2018)
        self.assertEqual(11850.00, t.get_personal_allowance())

    def test_total_taxable_income_zero_income(self):
        t = TaxYear(2017)
        self.assertEqual(0, t.get_taxable_income(0))

    def test_total_taxable_income_income_equals_personal_allowance(self):
        t = TaxYear(2017)
        self.assertEqual(0, t.get_taxable_income(11500))

    def test_total_taxable_income_income_over_personal_allowance_1(self):
        t = TaxYear(2017)
        self.assertEqual(1, t.get_taxable_income(11501))

    def test_total_taxable_income_income_over_personal_allowance_2(self):
        t = TaxYear(2017)
        self.assertEqual(20001, t.get_taxable_income(31501))

    def test_total_taxable_income_income_over_personal_allowance_3(self):
        t = TaxYear(2018)
        self.assertEqual(1.00, t.get_taxable_income(11851))

    def test_total_taxable_income_income_over_personal_allowance_4(self):
        t = TaxYear(2018)
        self.assertEqual(31650.00, t.get_taxable_income(43500))


if __name__ == '__main__':
    unittest.main()
