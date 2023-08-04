# Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting from zero up to n and return a new string.

'''
Analysis:
'Pynative' 4 
o/p = tive

if index >= 4:
add character to the output container
'''


def remove_char(string, no):
    output = ''
    for ind in range(len(string)):
        if ind >= no:
            output += string[ind]

    return output

# other solutions


print('pynative'[2:])


print(remove_char('pynative', 4))
print(remove_char('pynative', 2))
