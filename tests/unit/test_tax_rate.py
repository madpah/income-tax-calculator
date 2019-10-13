import unittest

from income_tax_calculator.tax_rate import TaxRate


class TestTaxRate(unittest.TestCase):
    _tax_rate_low = TaxRate('Low Tax Rate', 10.00, 0, 1000)
    _tax_rate_high = TaxRate('High Tax Rate', 25.00, 1000, 100000)

    def test_get_taxable_amount_zero_1(self):
        self.assertEqual(0.00, self._tax_rate_low.get_taxable_amount(0))

    def test_get_taxable_amount_zero_2(self):
        self.assertEqual(0.00, self._tax_rate_high.get_taxable_amount(1000))

    def test_get_taxable_amount_1(self):
        self.assertEqual(1.00, self._tax_rate_low.get_taxable_amount(1.00))

    def test_get_taxable_amount_2(self):
        self.assertEqual(1000.00, self._tax_rate_low.get_taxable_amount(1001.00))

    def test_get_taxable_amount_3(self):
        self.assertEqual(1.00, self._tax_rate_high.get_taxable_amount(1001.00))

    def test_get_tax_due_no_tax_due_zero_taxable_income_1(self):
        self.assertEqual(0.00, TaxRate.get_tax_due_for_tax_rate(0, self._tax_rate_low))

    def test_get_tax_due_no_tax_due_zero_taxable_income_2(self):
        self.assertEqual(0.00, TaxRate.get_tax_due_for_tax_rate(0, self._tax_rate_high))

    def test_get_tax_due_taxable_income_low_1(self):
        self.assertEqual(50.00, TaxRate.get_tax_due_for_tax_rate(500, self._tax_rate_low))

    def test_get_tax_due_taxable_income_low_2(self):
        self.assertEqual(100.00, TaxRate.get_tax_due_for_tax_rate(1000, self._tax_rate_low))

    def test_get_tax_due_taxable_income_low_3(self):
        self.assertEqual(100.00, TaxRate.get_tax_due_for_tax_rate(1001, self._tax_rate_low))

    def test_get_tax_due_taxable_income_high_1(self):
        self.assertEqual(0.25, TaxRate.get_tax_due_for_tax_rate(1001, self._tax_rate_high))


if __name__ == '__main__':
    unittest.main()
