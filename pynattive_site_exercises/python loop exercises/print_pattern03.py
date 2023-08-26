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
    for col in range(row + 1):
        if col >= (row // 2) + 1:
            break
        else:
            print('x', end=' ')

    for col2 in range(row - 1, 0, -1):
        print('*', end=' ')
    print()

    # Lets solve this bad boy tomorrow
