# Exercise 6: Display numbers divisible by 5 from a list

# Iterate the given list of numbers and print only those numbers which are divisible by 5


'''
0-10

1. Iterate through the numbers and then each number i m going to check if it is divisible by 5 of remainder is 0 or not.

ex. 0 % 5 == 0
then print i

'''

numbers = [10, 20, 33, 46, 55]

for each_num in numbers:
    if each_num % 5 == 0:
        print(each_num)
