# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second


'''
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

1. first get all the odd from l1
2. get all even from l2
3. append it to the new list
'''
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

new_list = []

for eachInd, eachNum in enumerate(l1):
    if eachInd % 2 != 0:
        new_list.append(eachNum)

for eachInd, eachNum in enumerate(l2):
    if eachInd % 2 == 0:
        new_list.append(eachNum)

print(new_list)

# Other solution using extend and slicing


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

l1 = l1[1::2]  # return odd index values
l2 = l2[0::2]  # return even index values

l3.extend(l1)
l3.extend(l2)

print(l3, 'l3')
