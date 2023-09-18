# Exercise 2: Concatenate two lists index-wise

'''
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
'''

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly", "don't"]

list3 = []

lst1_length = len(list1)
lst2_length = len(list2)


if lst1_length > lst2_length:
    lst = len(list1)
else:
    lst = len(list2)

for ind in range(lst):
    if lst1_length > ind and lst2_length > ind:
        list3.append(list1[ind]+list2[ind])
    elif lst1_length > ind:
        list3.append(list1[ind])
    else:
        list3.append(list2[ind])

print(list3)
