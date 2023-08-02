# Exercise 3: Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters that are present at an even index number.

'''
user = 'ashwin'

ahi

even = divisible by 2
'''

user_input = input('Enter the input: ')

print(f'Original string is {user_input}')
print('Printing only even index chars')

for i in range(len(user_input)):
    if i % 2 == 0:  # even
        print(user_input[i])
