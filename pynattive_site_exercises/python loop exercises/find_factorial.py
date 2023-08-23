# Exercise 13: Find the factorial of a given number

'''
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

5 = 5 * 4 * 3 * 2 * 1
'''

factorial = 1

inp = 5


if inp < 0:  # checking negative numbers
    print('Negative numbers are not allowed.')
elif inp == 0:  # checking number is 0 or not
    print('Factorial of 0 is 1')
else:  # number should be greater than 0
    while inp > 0:
        factorial *= inp
        inp -= 1

print(factorial)


# Using for loop
num = 5

for i in range(1, num + 1):
    # multiply factorial by current number
    factorial = factorial * i
print("The factorial of", num, "is", factorial)
