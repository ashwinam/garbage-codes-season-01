# Exercise 1A: Create a string made of the first, middle and last character

'''
str1 = "James"

op jms

[0]
[-1]

len(str1) // 2
'''


def newString(string):
    first_char = string[0]
    middle_char = string[len(string)//2]
    last_char = string[-1]

    return first_char+middle_char+last_char


result = newString("James")

print(result)


# Other solution

str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)
