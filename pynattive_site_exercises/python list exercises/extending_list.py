# Exercise 8: Extend nested list by adding the sublist

'''
You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
'''

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

'''
?Indexing

list[0] = a
list[1] = b
list[2] = ["c", ["d", "e", ["f", "g"], "k"], "l"]
list[2][0] = c
list[2][1] = ["d", "e", ["f", "g"], "k"]
list[2][1][0] = d
list[2][1][1] = e
list[2][1][2] = ["f", "g"]
'''

list1[2][1][2].extend(sub_list)
print(list1)
