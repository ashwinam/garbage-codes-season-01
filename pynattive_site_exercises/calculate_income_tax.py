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
