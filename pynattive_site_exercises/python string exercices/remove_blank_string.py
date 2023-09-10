# Exercise 14: Remove empty strings from a list of strings


'''
loop through the sentence and 
    each word check truthy falsy value.
    append it to a new word then print it
'''

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print([each_word for each_word in str_list if each_word])
