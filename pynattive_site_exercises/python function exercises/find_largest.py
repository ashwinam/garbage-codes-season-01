# Exercise 9: Find the largest item from a given list


'''
x = [4, 6, 8, 24, 12, 2]

0 < 4 = 4
4 < 6 = 6
6 < 8 = 8
8 < 24 = 24
24 < 12 = -
24 < 2 = -

24

'''


def find_largest(lst):
    largest = 0

    for num in lst:
        if largest < num:
            largest = num

    return largest


x = [4, 6, 8, 24, 12, 2]
result = find_largest(x)

# other solution

print(max(x))

print(result)
