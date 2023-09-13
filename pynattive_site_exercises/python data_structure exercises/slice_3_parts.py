# Exercise 3: Slice list into 3 equal chunks and reverse each chunk


'''
9 item
0: 3, 
3: 6, 
6: 9
'''
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
length = len(sample_list) / 3

for _ in range(0, 10):
    if _ % 3 == 0:
        print(_)
