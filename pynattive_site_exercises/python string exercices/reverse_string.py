# Exercise 11: Reverse a given string

str1 = 'PYnative'

reverse_string = ''
for each_char in range(len(str1)-1, -1, -1):
    reverse_string += str1[each_char]

print(reverse_string)
