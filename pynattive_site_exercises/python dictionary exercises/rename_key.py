# Exercise 8: Rename key of a dictionary

'''
Write a program to rename a key city to a location in the following dictionary.
'''

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

list_of_keys = list(sample_dict.keys())

list_of_keys[list_of_keys.index('city')] = 'location'

list_of_values = list(sample_dict.values())

new_dict = {}


for k, v in zip(list_of_keys, list_of_values):
    new_dict[k] = v

print(new_dict)
