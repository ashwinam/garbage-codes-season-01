# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

'''
range = 4 -- 30

[num for num in range(4, 30) if num % 2 == 0]
'''

lst = [num for num in range(4, 30) if num % 2 == 0]

print(lst)

# other solution

print(list(range(4, 30, 2)))
