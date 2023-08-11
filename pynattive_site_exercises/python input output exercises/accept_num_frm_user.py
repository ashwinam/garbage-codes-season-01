# Exercise 1: Accept numbers from a user

# Write a program to accept two numbers from the user and calculate multiplication

first_num = int(input('Please, provide a first number: '))
second_num = int(input('Please, provide a second number: '))


def calculate_multiplication(f_num, s_num):
    return f_num * s_num


result = calculate_multiplication(first_num, second_num)

print(result, 'result')
