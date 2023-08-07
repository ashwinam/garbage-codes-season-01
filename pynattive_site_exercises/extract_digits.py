# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

'''
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

1. using math extracting remainder
2. insert it into list 
3. join with a space
'''

a_number = 7536


def extract_digits(number):
    lst = []

    while number > 0:
        remainder = number % 10
        number = number // 10
        lst.append(remainder)

    return ' '.join(list(map(lambda x: str(x), lst)))


print(extract_digits(a_number))
