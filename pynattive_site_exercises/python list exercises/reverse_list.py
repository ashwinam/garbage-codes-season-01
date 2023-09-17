# Exercise 1: Reverse a list in Python


'''
1. take a list, use a reverse method for reversing list.

2. using slicing, to reverse a list.

3. loop reverse and then using index to reversing a list.
'''

list1 = [100, 200, 300, 400, 500]

# list1.reverse()

print(list1)

# using slicing

print(list1[::-1])

# using loop

list1 = [100, 200, 300, 400, 500]

print([list1[ele] for ele in range(len(list1) - 1, -1, -1)])
