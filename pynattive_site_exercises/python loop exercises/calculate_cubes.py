# Exercise 16: Calculate the cube of all numbers from 1 to a given number

'''
Write a program to print the cube of all numbers from 1 to a given number
1, 6


'''

CUBE = 3
SQUARE = 2
input_number = 6

for num in range(1, 7):
    print(
        f'Current Number is : {num} and the cube is {num ** 3}')
