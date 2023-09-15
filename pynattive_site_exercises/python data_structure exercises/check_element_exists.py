# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 97, 95]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print(95 not in list(sample_dict.values()))

for number in roll_number:
    if number not in list(sample_dict.values()):
        roll_number.remove(number)

print(roll_number)
