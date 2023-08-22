# Exercise 12: Display Fibonacci series up to 10 terms

'''
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.


'''
# set up the positions with values
pre_num = 0
current_num = 1

for num in range(10):
    # print the first value
    print(pre_num, end=', ')

    # calculate current position
    total = pre_num + current_num

    # updating values
    pre_num = current_num
    current_num = total
