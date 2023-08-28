# Exercise 2: Create a function with variable length of arguments

'''
 call function with 3 arguments
func1(20, 40, 60)

o/p 
Printing values
20
40
60
'''


def func(*args):
    print('Printing values')
    for i in args:
        print(i)


func(10, 20, 30, 40, 50)
