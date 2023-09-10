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


# Other solution


str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)
