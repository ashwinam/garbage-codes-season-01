# Exercise 3: Slice list into 3 equal chunks and reverse each chunk


'''
9 item
0: 3, 
3: 6, 
6: 9
'''
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
lst_length = len(sample_list)

parting_size = lst_length // 3

lst1 = []
lst2 = []
lst3 = []

for i in range(0, lst_length):
    if i < parting_size:
        lst1.append(sample_list[i])
    elif i < (2 * parting_size):
        lst2.append(sample_list[i])
    else:
        lst3.append(sample_list[i])

lst1.reverse()
print(lst1)
lst2.reverse()
print(lst2)
lst3.reverse()
print(lst3)
