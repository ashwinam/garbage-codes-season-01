# Exercise 5: Create an inner function to calculate the addition in the following way


'''
1. Create an outer function that will accept two parameters, a and b
2. Create an inner function inside an outer function that will calculate the addition of a and b
3. At last, an outer function will add 5 into addition and return it
'''


def out_func(a, b):
    def inner_func():
        res = a + b
        return res
    return inner_func() + 5


op = out_func(20, 10)

print(op)
