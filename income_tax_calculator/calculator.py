import argparse
import os

from income_tax_calculator.tax_year import TaxYear, NoTaxYearSuppliedException, UnknownTaxYearException

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser('Calculate Income Tax')
    arg_parser.add_argument('tax_year', metavar="TAX_YEAR", type=int, help="Tax Yar to calculate Income Tax for")
    arg_parser.add_argument('gross_income', metavar="GROSS_INCOME", type=float, help="Gross Income")
    args = arg_parser.parse_args()

    # Set the path to our data
    TaxYear.set_data_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/rates.json'))

    # Create our TaxYear instance based on user input
    try:
        t = TaxYear(args.tax_year)
    except NoTaxYearSuppliedException:
        print("Not Tax Year was supplied - please try again.")
        exit(1)
    except UnknownTaxYearException:
        print("The supplied Tax Year '{}' is not known.".format(args.tax_year))
        exit(2)

    # Print out our calculation
    t.print_calculation(gross_income=args.gross_income)

    # Exit cleanly
    exit(0)
