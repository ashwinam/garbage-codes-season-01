# Exercise 15: Use a loop to display elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for ind, ele in enumerate(my_list):
    if ind % 2 != 0:
        print(ele, end=' ')


# Other solution using slicing

for ele in my_list[1::2]:
    print(ele, end=' - ')
