# Exercise 4: Count the occurrence of each element from a list


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]


def return_occurances(lst):
    result = {}
    for ele in lst:
        if ele not in result:
            result[ele] = 1
        else:
            result[ele] += 1

    return result


result = return_occurances(sample_list)
print(result)
