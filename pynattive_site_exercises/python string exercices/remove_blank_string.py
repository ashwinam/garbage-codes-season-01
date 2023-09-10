# Exercise 14: Remove empty strings from a list of strings


'''
loop through the sentence and 
    each word check truthy falsy value.
    append it to a new word then print it
'''

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print([each_word for each_word in str_list if each_word])


# Other solution
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)
