# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)

'''
ex 
* * * * *
* * * *
* * *
* *
*

1. first iteration
    reverse order like 5, 4 ,3,2,1
2. second iteration 4, 3, 2, 1
and so on.

'''


for i in range(5, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
