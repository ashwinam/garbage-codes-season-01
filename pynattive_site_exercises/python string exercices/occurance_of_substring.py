# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

'''
Write a program to find all occurrences of “USA” in a given string ignoring the case.

1. serating the words from sentences.
2. loop through this list of words
    a. create dictionary 
    b. check if word is already in dictionary key or not
        i. if yes then just add +1 
        ii. else create a key
'''

str1 = "Welcome to USA . usa awesome, isn't it?"


def finding_occurances_of_substring(string):
    # split string into words
    list_of_words = string.split()
    result_dictionary = {}
    for word in list_of_words:
        if word.lower() in result_dictionary:
            result_dictionary[word.lower()] += 1
        else:
            result_dictionary[word.lower()] = 1
    print('The USA count is, ', result_dictionary['usa'])


finding_occurances_of_substring(str1)
