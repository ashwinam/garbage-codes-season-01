# Exercise 18: Replace each special symbol with # in the following string

import string

str1 = '/*Jon is @developer & musician!!'

result = ''

for char in str1:
    if char in string.punctuation:
        result += '#'
    elif char.isalpha():
        result += char
    elif char.isspace():
        result += char

print(result)
