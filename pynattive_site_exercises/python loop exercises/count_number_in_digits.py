# Exercise 6: Count the total number of digits in a number


'''
For example, the number is 75869, so the output should be 5.

# seperate the each numbers by divisible by 10, it return the remainder.
# count the each iteration
'''

num = 789456123


count = 0

while num > 0:
    num = num // 10

    count += 1

print(count)
