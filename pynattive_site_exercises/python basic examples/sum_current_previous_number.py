# Exercise 2: Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

'''
i = 0, p = 0
i + p
p = i

i = 1, p = 0
i + p = 1
p = i

...
'''

previous_num = 0

print('Printing current and previous number sum is a range(10)')
for current_num in range(10):
    print(
        f'Current Number {current_num} Previous Number {previous_num} Sum: {current_num + previous_num}')

    previous_num = current_num
