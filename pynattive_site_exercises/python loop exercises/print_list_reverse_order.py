# Exercise 8: Print list in reverse order using a loop

'''
Given: 
list1 = [10, 20, 30, 40, 50]

o/p
50
40
30
20
10

'''

lst = [10, 20, 30, 40, 50]

for num in range(len(lst) - 1, -1, -1):
    print(lst[num])
