# Exercise 7: Print the following pattern

# Write a program to use for loop to print the following reverse number pattern

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

outer loop: 5 times
inner loop :
    1st iteration 5 times
    2nd iteration 4 times
    3rd iteration 3 times
    4th iteration 2 times
    5th iteration 1 time
numbers are also goes in reverse order
'''

for row in range(5):
    for col in range(5-row, 0, -1):
        print(col, end=' ')
    print()
