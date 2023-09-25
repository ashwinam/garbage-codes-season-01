# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

'''
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
'''

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

res = {}

for key in keys:
    if key in sample_dict:
        res[key] = sample_dict[key]

print(res)


# Other solution

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)
