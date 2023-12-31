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

# Other solution

print('------------------')
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")


for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
