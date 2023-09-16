# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_list = []

for ele in sample_list:
    if ele not in unique_list:
        unique_list.append(ele)

tuple_ele = tuple(unique_list)

# maximum
print(max(tuple_ele))

# Minimum
print(min(tuple_ele))


# Other solutions

maximum = 0

for ele in tuple_ele:
    if maximum < ele:
        maximum = ele

print(maximum, 'maximm')

# minimum

minimum = tuple_ele[0]
for ele in tuple_ele:
    if minimum > ele:
        minimum = ele

print(minimum, 'minimm')
