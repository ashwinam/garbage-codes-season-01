# Exercise 4: Write a program to print multiplication table of a given number

'''
For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20
'''

user_inp = int(input('Enter a number: '))

for num in range(1, 11):
    print(user_inp * num)
