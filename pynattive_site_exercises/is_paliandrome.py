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


def is_paliandrome_using_remainder_calculation(n_inp):
    original_number = n_inp

    reverse_number = 0
    while n_inp > 0:
        remainder = n_inp % 10
        n_inp = n_inp // 10

        reverse_number = (reverse_number * 10) + remainder
        '''
        above calculation
        (0 * 10) + 5 = 5
        (5 * 10) + 2 = 52
        (52 * 10) + 5 = 525
        '''

    return original_number == reverse_number


is_paliandrome_num = is_paliandrome_using_remainder_calculation(525)

if is_paliandrome_num:
    print('Given number is paliandrome.')
else:
    print('Not a prime number.')
