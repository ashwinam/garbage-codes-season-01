# Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

output = {}

for employee in employees:
    output[employee] = defaults

print(output)

print({k: defaults for k in employees})

# Other solution

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res)

print(dict.fromkeys('Rahul', '123'))
