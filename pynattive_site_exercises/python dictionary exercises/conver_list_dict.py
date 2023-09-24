# Exercise 1: Convert two lists into a dictionary

'''
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value.
'''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print({k: v for k, v in zip(keys, values)})

# Usint dict function
print(dict(zip(keys, values)))
