# Exercise 15: Remove special symbols / punctuation from a string

'''
Loop Through sentences.split('')
    check is aplhabet or not
        if true then add to the list
'''

import string
str1 = "/*Jon is @developer & musician"

result = ''
for char in str1:
    if char.isalpha():
        result += char
    elif char.isspace():
        result += char

print(result)


# Other solution using string punctuation


str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)
