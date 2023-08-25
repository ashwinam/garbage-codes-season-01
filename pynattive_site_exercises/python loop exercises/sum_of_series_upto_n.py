# Exercise 17: Find the sum of the series upto n terms

'''
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

n = 5

1 2 3 4 5

0 + 1 * 10 10
10 + 2 * 10 120
120 + 3 *10 1230
1230 + 4 * 10 12340
12340 + 5 *10 123450

0 * 10 + 1 1
1 * 10 + 2 12
12 * 10 + 3 123
123 * 10 + 4 1234
1234 * 10 + 5 12345



'''

sol = 0


for i in range(5):
    temp = 0
    for j in range(i+1):
        temp = (temp * 10) + 2
    sol += temp


print(sol, '>>>>')


# other solution

n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)
