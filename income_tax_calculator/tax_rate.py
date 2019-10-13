class TaxRate:
    _name = None
    _percentage = None
    _start = None
    _end = None

    def __init__(self, name, rate_percentage, start, end=None):
        """
        Constructor

        :type name: str
        :type rate_percentage: float
        :type start: float
        :type end: float|None
        """
        self._name = name
        self._percentage = rate_percentage
        self._start = start
        if end:
            self._end = end

    @staticmethod
    def get_tax_due_for_tax_rate(taxable_income: int, tax_rate: object):
        """

        :type taxable_income: float
        :type tax_rate: TaxRate
        """
        return round((tax_rate.get_taxable_amount(taxable_income) * (tax_rate.get_percentage() / 100)), 2)

    def get_taxable_amount(self, taxable_income):
        """
        Calculates the amount of Income Tax due for this rate based on the supplied taxable income amount supplied

        Taxable Income is Gross Income after any allowances have been deducted.

        :type taxable_income: float
        """
        # Default that this TaxRate is no applicable to the supplied taxable income
        amount_taxable_at_rate = 0

        # If the total taxable income is inside this Tax Rate
        if taxable_income > 0 and taxable_income >= self._start:
            # If this Tax Rate has an upper limit and this taxable income is over this limit
            if self._end and taxable_income >= self._end:
                amount_taxable_at_rate = (self._end - self._start)
            # Else compute the taxable amount within the rate limits
            else:
                amount_taxable_at_rate = (taxable_income - self._start)

        return amount_taxable_at_rate

    def get_percentage(self):
        return self._percentage

    def get_name(self):
        return self._name

    def __repr__(self):
        return '<TaxRate name={}, percentage={}, start={}, end={}>'.format(self._name, self._percentage, self._start,
                                                                           self._end)
