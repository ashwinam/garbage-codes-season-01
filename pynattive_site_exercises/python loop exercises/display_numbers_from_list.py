# Exercise 5: Display numbers from a list using loop

'''
Write a program to display only those numbers from a list that satisfy the following conditions

1. The number must be divisible by five
2. If the number is greater than 150, then skip it and move to the next number
3. If the number is greater than 500, then stop the loop
'''

lst = [12, 75, 150, 180, 145, 525, 50]

for num in lst:
    if num % 5 == 0:
        if num > 500:
            break
        if num > 150:
            continue
        print(num)

# Other solution

numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)
