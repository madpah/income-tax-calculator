import argparse

from income_tax_calculator.tax_year import TaxYear

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser('Calculate Income Tax')
    arg_parser.add_argument('tax_year', metavar="TAX_YEAR", type=int, help="Tax Yar to calculate Income Tax for")
    arg_parser.add_argument('gross_income', metavar="GROSS_INCOME", type=float, help="Gross Income")
    args = arg_parser.parse_args()

    t = TaxYear(args.tax_year)
