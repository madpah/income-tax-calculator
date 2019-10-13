import unittest

from income_tax_calculator.tax_rate import TaxRate


class TestTaxRate(unittest.TestCase):
    _tax_rate_low = TaxRate(name='Low Tax Rate', rate_percentage=10.00, start=0, end=1000)
    _tax_rate_high = TaxRate(name='High Tax Rate', rate_percentage=25.00, start=1000, end=100000)
    _tax_rate_top_rate = TaxRate(name='Top Rate Tax', rate_percentage=27.00, start=10000)
    _tax_rate_higher = TaxRate(name='Higher rate', rate_percentage=40.00, start=31581, end=150000)

    def test_get_taxable_amount_zero_1(self):
        self.assertEqual(0.00, TestTaxRate._tax_rate_low.get_taxable_amount(taxable_income=0))

    def test_get_taxable_amount_zero_2(self):
        self.assertEqual(0.00, TestTaxRate._tax_rate_high.get_taxable_amount(taxable_income=1000))

    def test_get_taxable_amount_1(self):
        self.assertEqual(1.00, TestTaxRate._tax_rate_low.get_taxable_amount(taxable_income=1.00))

    def test_get_taxable_amount_2(self):
        self.assertEqual(1000.00, TestTaxRate._tax_rate_low.get_taxable_amount(taxable_income=1001.00))

    def test_get_taxable_amount_3(self):
        self.assertEqual(1.00, TestTaxRate._tax_rate_high.get_taxable_amount(taxable_income=1001.00))

    def test_get_taxable_amount_4(self):
        self.assertEqual(69.00, TestTaxRate._tax_rate_higher.get_taxable_amount(taxable_income=31650.00))

    def test_get_tax_due_no_tax_due_zero_taxable_income_1(self):
        self.assertEqual(0.00, TaxRate.get_tax_due_for_tax_rate(taxable_income=0, tax_rate=TestTaxRate._tax_rate_low))

    def test_get_tax_due_no_tax_due_zero_taxable_income_2(self):
        self.assertEqual(0.00, TaxRate.get_tax_due_for_tax_rate(taxable_income=0, tax_rate=TestTaxRate._tax_rate_high))

    def test_get_tax_due_taxable_income_low_1(self):
        self.assertEqual(50.00,
                         TaxRate.get_tax_due_for_tax_rate(taxable_income=500, tax_rate=TestTaxRate._tax_rate_low))

    def test_get_tax_due_taxable_income_low_2(self):
        self.assertEqual(100.00,
                         TaxRate.get_tax_due_for_tax_rate(taxable_income=1000, tax_rate=TestTaxRate._tax_rate_low))

    def test_get_tax_due_taxable_income_low_3(self):
        self.assertEqual(100.00,
                         TaxRate.get_tax_due_for_tax_rate(taxable_income=1001, tax_rate=TestTaxRate._tax_rate_low))

    def test_get_tax_due_taxable_income_high_1(self):
        self.assertEqual(0.25,
                         TaxRate.get_tax_due_for_tax_rate(taxable_income=1001, tax_rate=TestTaxRate._tax_rate_high))

    def test_get_tax_due_taxable_income_top_rate_1(self):
        self.assertEqual(2700, TaxRate.get_tax_due_for_tax_rate(taxable_income=20000,
                                                                tax_rate=TestTaxRate._tax_rate_top_rate))


if __name__ == '__main__':
    unittest.main()
