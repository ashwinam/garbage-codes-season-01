# Exercise 9: Calculate the sum and average of the digits present in a string

'''
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

1. loop through string
2. check each character , is digit or not
3. addition in a varibale
4. for average count also taking it.
'''

str1 = "PYnative29@#8496"


def sum_average_digits_in_string(string):
    sum_digits = 0
    count = 0

    for each_char in string:
        if each_char.isdigit():
            sum_digits += int(each_char)
            count += 1

    print(f'{sum_digits} Average is {sum_digits / count}')


sum_average_digits_in_string(str1)
