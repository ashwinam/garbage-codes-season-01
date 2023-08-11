# Exercise 7: Return the count of a given substring from a string

# Write a program to find how many times substring “Emma” appears in the given string.

'''
"Emma is good developer. Emma is a writer"

emma appeared two times
'''

# using count method

str_ex = "Emma is good developer. Emma is a writer"

print(str_ex.count('Emma'))

# using from scratch


def count_substring_in_string(string, substring):
    list_of_words = string.split(' ')

    count = 0
    for word in list_of_words:
        if substring == word:
            count += 1

    return count


print(count_substring_in_string(str_ex, 'Emma'), 'times')


def count_emma(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i: i + 4] == substring:
            '''
            0 : 0 + 4 = 0:4
            1 : 1 + 4 = 1:5
            2 : 2 + 4 = 2:6
            '''
            count += 1

    return count


print('Emma appeared', count_emma(str_ex, 'Emma'), 'times')
