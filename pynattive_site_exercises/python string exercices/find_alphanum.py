# Exercise 17: Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"

print('\n'.join([char for char in str1.split() if not char.isalpha()]))
