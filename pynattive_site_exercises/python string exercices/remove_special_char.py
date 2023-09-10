# Exercise 15: Remove special symbols / punctuation from a string

'''
Loop Through sentences.split('')
    check is aplhabet or not
        if true then add to the list
'''

str1 = "/*Jon is @developer & musician"

result = ''
for char in str1:
    if char.isalpha():
        result += char
    elif char.isspace():
        result += char

print(result)
