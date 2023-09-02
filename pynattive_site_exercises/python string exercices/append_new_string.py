# Exercise 2: Append new string in the middle of a given string

'''
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

divide and then join

1. find the middle character
2. seperate 
    i.starting to middle char
    ii. New string
    iii. from middle to last
3. concatenate every char

ex "Auly" & "Ashwin"
l = 2
"Auly"[0,2]  = Au
"Auly"[2,(len)] ly

"AuAshwinly"
'''


def append_new_string(str1, str2):
    # seperate the first string

    middle_index = len(str1) // 2

    left_char = str1[0:middle_index]
    middle_char = str2
    right_side = str1[middle_index:len(str1)]

    # join sentences together
    return left_char+middle_char+right_side


result = append_new_string('Auly', 'Kelly')

print(result)
