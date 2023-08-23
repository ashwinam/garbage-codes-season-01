# Exercise 14: Reverse a given integer number

'''
getting remainder then adding with decimal
'''


inp = 76542

op = 0
while inp > 0:
    remainder = inp % 10
    inp = inp // 10

    op = (op * 10) + remainder

print(op, '*****')
