# Exercise 7: Add new item to list after a specified item

'''
Write a program to add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# temp_list = []

# for lst in list1:
#     if isinstance(lst, list):
#         if 6000 in lst:
#             lst.append(7000)
#             temp_list.append(lst)
#         else:
#             for row in lst:
#                 if isinstance(row, list):
#                     if 6000 in row:
#                         row.append(7000)
#                         temp_list.append(lst)
#                     else:
#                         lst.append(row)
#                         temp_list.append(lst)
#                 else:
#                     lst.append(row)
#                     temp_list.append(lst)
#     else:
#         temp_list.append(lst)

# print(temp_list, '>>>>')

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

# solution
list1[2][2].append(7000)
print(list1)
