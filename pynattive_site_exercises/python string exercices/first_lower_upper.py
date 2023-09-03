# Exercise 4: Arrange string characters such that lowercase letters should come first


'''
first getting all lowers
then getting all upper

concatenate lower+upper
'''


def arrange_string_lower_to_upper(string):
    lower_str = ''
    upper_str = ''

    for each_char in string:
        if each_char.islower():
            lower_str += each_char
        else:
            upper_str += each_char

    return lower_str + upper_str


result = arrange_string_lower_to_upper('PyNaTive')

print(result)

# Other Solution

str1 = "PYnAtivE"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)
