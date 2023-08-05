# Exercise 8: Print the following pattern

'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''


for i in range(5):
    for j in range(i + 1):
        print(i + 1, end=' ')
    print()


'''
 i = 0, j = 1
 1
 i = 1, j = 2: j two times
  1 + 1 =2
2 times 2 , 2
i = 2, j = 3: j three times
2 + 1 = 3
three times 3, 3, 3
i = 3, j = i +1 = 4: j four times
3 + 1 = 4
four times 4, 4, 4, 4
i = 4, j = i + 1 = 5: j five times
4 + 1 = 5
five times 5, 5, 5, 5, 5
'''
