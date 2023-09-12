# Exercise 5: Create a Python set such that it shows the element from both lists in a pair

'''
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

expected:
Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
'''


first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = set()

for f_num, s_num in zip(first_list, second_list):
    result.add((f_num, s_num))

print('Result is ', result)


# Other solution

first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List ", first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)
