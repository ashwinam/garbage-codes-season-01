# Exercise 18: Print the following pattern


'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*


'''

for row in range(9):
    if row < 5:
        for col in range(row + 1):
            print('x', end=' ')

    if row >= 5:
        for col2 in range(9-row):
            print('x', end=' ')
    print()

    # Lets solve this bad boy tomorrow
