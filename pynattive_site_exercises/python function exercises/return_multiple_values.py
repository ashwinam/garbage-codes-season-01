# Exercise 3: Return multiple values from a function

'''
Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

addition_result = a + b
subtraction_result = a - b 

return addition, subtraction
'''


def calculation(f_num, s_num):

    return f_num + s_num, f_num - s_num


result = calculation(20, 10)

print(result)
