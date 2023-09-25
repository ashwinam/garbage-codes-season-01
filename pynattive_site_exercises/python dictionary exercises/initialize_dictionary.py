# Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

output = {}

for employee in employees:
    output[employee] = defaults

print(output)
