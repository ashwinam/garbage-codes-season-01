# Exercise 5: Count all letters, digits, and special symbols from a given string

'''
checking each characteris aplpha, digits or symbols
'''

str1 = "P@#yn26at^&i5ve"


chars = 0
digits = 0
symbols = 0

for each_char in str1:
    if each_char.isalpha():
        chars += 1
    elif each_char.isdigit():
        digits += 1
    else:
        symbols += 1

print(chars)
print(digits)
print(symbols)
