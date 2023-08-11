# Exercise 5: Check if the first and last number of a list is the same

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

'''
[10, 20, 30, 40, 10]

extract first and lst number from list

compare both of them

return true or false

'''


def compare_first_last(numbs: list):
    first_num = numbs[0]
    last_num = numbs[-1]

    return first_num == last_num


print(compare_first_last([10, 20, 30, 40, 50]))
