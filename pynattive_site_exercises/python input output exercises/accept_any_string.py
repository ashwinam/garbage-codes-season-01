# Exercise 7: Accept any three string from one input() call

# Write a program to take three names as input from a user in the single input() function call.

'''
Take a input using spaces and then split it 
'''


user_input = input('Enter three string: ')


for name in user_input.split(' '):
    print('Name: ', name)
