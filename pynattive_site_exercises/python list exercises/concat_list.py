# Exercise 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

solution = []

for first_ele in list1:
    for second_ele in list2:
        solution.append(first_ele + ' ' + second_ele)

print(solution)
