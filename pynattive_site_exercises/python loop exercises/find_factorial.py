# Exercise 13: Find the factorial of a given number

'''
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

5 = 5 * 4 * 3 * 2 * 1
'''

res = 1

inp = 5

while inp > 0:
    res *= inp
    inp -= 1

print(res)
