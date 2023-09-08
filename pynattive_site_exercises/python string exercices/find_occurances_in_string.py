# Exercise 10: Write a program to count occurrences of all characters within a string

'''
str1 = "Apple"  

Expected output:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
'''


def find_occurances(string):
    all_occuraces = {}

    for each_char in string:
        if each_char in all_occuraces:
            all_occuraces[each_char] += 1
        else:
            all_occuraces[each_char] = 1
    return all_occuraces


result = find_occurances("Apple")

print(result)
