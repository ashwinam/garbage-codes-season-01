# Exercise 12: Calculate income tax for the given income by adhering to the below rules

'''
Rules:

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20

For example, suppose the taxable income is 45000 the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.

45000 - 10000 = 35000 - 10000 = 25000 * 20%

'''


def calculate_tax(income):
    remaining_income = max(0, income - 20000)

    ten_percent_bracket = max(0, income - 10000)

    taxable_amount = 0

    if remaining_income:
        taxable_amount += (remaining_income * 0.20)
        taxable_amount += (10000 * 0.10)
        return taxable_amount
    elif max(0, ten_percent_bracket):  # for 10% balance
        taxable_amount += (ten_percent_bracket * 0.10)
        return taxable_amount
    else:
        return ('No tax is payable')


print(calculate_tax(29000))


# Better solution

def calculate_accurate_tax(taxable_income):

    tax_payable = 0

    if taxable_income <= 10000:
        tax_payable = 0
    elif taxable_income <= 20000:
        income = taxable_income - 10000
        tax_payable = income * 0.10
    else:
        tax_payable = 10000 * 0.10
        remainig_income = taxable_income - 20000

        tax_payable += remainig_income * 0.20

    return f'Total tax payable is {tax_payable}'


print(calculate_accurate_tax(25000))
