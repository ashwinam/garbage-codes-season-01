# Exercise 2: Merge two Python dictionaries into one

'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
print(dict1)

# using loop

for k, v in dict2.items():
    dict1[k] = v

print(dict1)
