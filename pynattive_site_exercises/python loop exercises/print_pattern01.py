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

# solution from pynative

print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")
