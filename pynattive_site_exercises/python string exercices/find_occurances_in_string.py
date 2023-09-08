# Exercise 10: Write a program to count occurrences of all characters within a string

'''
str1 = "Apple"  

Expected output:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
'''


from collections import Counter


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
# ---------- Other solution Using collection module -----------

str1 = "AppleA"

print(Counter(str1))

# Other solution

str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)
