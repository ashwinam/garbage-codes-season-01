# Exercise 2: Print the following pattern

# Write a program to print the following number pattern using a loop.


'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

rows = 5
whatever the row counter is then print the column

'''


for row in range(5):
    for col in range(row + 1):
        print(col + 1, end=' ')
    print()
