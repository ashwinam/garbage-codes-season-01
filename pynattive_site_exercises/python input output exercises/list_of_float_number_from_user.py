# Exercise 5: Accept a list of 5 float numbers as an input from the user

'''
take the input from user using spaces
* use the split and then add into the list with float of
'''

user_list = input('Provide a multiple input using spaces: ')

print([float('%.2f' % float(num)) for num in user_list.split(' ')])

# if user want to put single numbers at a time

numbers = []

for num in range(5):

    print('Enter the numbers at this location ', num, ':')
    number = float(input())

    numbers.append(number)

print(numbers)
