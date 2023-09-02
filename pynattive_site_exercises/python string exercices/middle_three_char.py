# Exercise 1B: Create a string made of the middle three characters

'''
1. find the middle char
2. slicing [middle_char - 1: middle_char + 2]
'''


def middleThreeChar(string):
    middle_char_index = len(string) // 2

    return string[middle_char_index - 1: middle_char_index + 2]


result = middleThreeChar("JhonDipPeta")
result = middleThreeChar("JaSonAy")

print(result)
