# Exercise 16: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
result = ''

for char in str1:
    if char.isdigit():
        result += char

print(result)
