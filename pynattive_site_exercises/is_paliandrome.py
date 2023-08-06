# Exercise 9: Check Palindrome Number

# Write a program to check if the given number is a palindrome number.

'''
A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

1. reverse a number
    a. make it string
    b. reverse it using method
    then jump to second step.
    without using string 
    1. decimal number base is 10, divide by 10
    2. so it will return a last number every time from sequence of numbers, then add it by multiplying 10.
    then second step
2. compare the number with original one
    a. if true then its paliandrome
'''


def is_paliandrome(num_input):
    convert_input = list(str(num_input))
    convert_input.reverse()
    reversed_input = int(''.join(convert_input))
    return num_input == reversed_input


print(is_paliandrome(121))
