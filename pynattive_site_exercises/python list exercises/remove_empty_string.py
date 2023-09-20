# Exercise 6: Remove empty strings from the list of strings

'''

'''

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print(list(filter(lambda x: x, list1)))


# using list comprehension
print([ele for ele in list1 if ele])

# Other solution

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)
