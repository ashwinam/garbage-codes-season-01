# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

# calculate the product
# check the product >= 1000, then return product else sum of two numbers

number1 = 40
number2 = 30

product = number1 * number2

if product <= 1000:
    print('Answer is: ', product)
else:
    print('Answer is: ', number1 + number2)
