# Exercise 3: Create a new string made of the first, middle, and last characters of each input string

'''
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

- create seperate function for getting first, middle and last char

- merge them into one

'''


def first_char_str(string):
    return string[0]


def middle_char_str(string):
    middle_index = len(string) // 2
    return string[middle_index]


def last_char_str(string):
    return string[-1]


s1 = "America"
s2 = "Japan"


new_str = ''

# First Char from both string

f_string = first_char_str(s1) + first_char_str(s2)
new_str += f_string

# Middle Char from both string

m_string = middle_char_str(s1) + middle_char_str(s2)

new_str += m_string

# Last char from both string
l_string = last_char_str(s1) + last_char_str(s2)
new_str += l_string

print(new_str)
