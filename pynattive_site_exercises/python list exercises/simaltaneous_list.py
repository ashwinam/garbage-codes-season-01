# Exercise 5: Iterate both lists simultaneously

'''
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
'''

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2.reverse()

for ele1, ele2 in zip(list1, list2):
    print(ele1, ele2)
