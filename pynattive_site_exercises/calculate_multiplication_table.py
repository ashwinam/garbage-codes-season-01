# Exercise 13: Print multiplication table form 1 to 10

'''
two loop
1 number will constant till second loop counts

1 - 10 first loop
1 - 10 second loop

'''


def multiplication_table(start, end):
    for num in range(start, end):
        for num2 in range(start, end):
            print(num * num2, end=' ')
        print()


multiplication_table(1, 11)
