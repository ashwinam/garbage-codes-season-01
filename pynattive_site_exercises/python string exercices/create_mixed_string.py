# Exercise 6: Create a mixed String using the following rules

'''
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"

s3 = ?

1. both are same length
    - loop range(len(s1)) in i
    - in s1 indexing start from i
    - in s2 indexing start from len(s2) - i
'''

s1 = "Abcd"
s2 = "Vwxyz"
s3 = ''
for ind in range(len(s1)):
    if len(s1) != len(s2):
        print('Error! Length should be same.')
        break
    s3 += s1[ind]
    s3 += s2[len(s2) - (ind + 1)]
else:
    print(s3, '>>>>>>')

# Other solution

s1Length = len(s1)
s2Length = len(s2)

# max length

length = s1Length if s1Length > s2Length else s2Length

# reverse the s2
s2 = s2[::-1]

op = ''

for i in range(length):
    if i < s1Length:
        op += s1[i]
    if i < s2Length:
        op += s2[i]

print(op)
