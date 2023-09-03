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
