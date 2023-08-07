# Exercise 10: Create a new list from a two list using the following condition

'''
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

a_lst = [10, 20, 25, 30, 35] # extract odd numbers
b_lst = [40, 45, 60, 75, 90] # extract even numbers

nw_lst = [25, 35] # from first list
nw_lst = [40, 60, 90] # from first list

#merge those two list
new_lst = [25, 35, 40, 60, 90]

condition for odd 
1. if number is divisible by 2 its even
    else odd
'''


a_lst = [10, 20, 25, 30, 35]  # extract odd numbers
b_lst = [40, 45, 60, 75, 90]  # extract even numbers

new_list = []

for num in a_lst:
    if num % 2 != 0:
        new_list.append(num)

for num in b_lst:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)
