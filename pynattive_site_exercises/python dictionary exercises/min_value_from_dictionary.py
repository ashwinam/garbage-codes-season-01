# Exercise 9: Get the key of a minimum value from the following dictionary

sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

min_value = min(sample_dict.values())

for k, v in sample_dict.items():
    if v == min_value:
        print(k)

# Other solution
print(min(sample_dict, key=sample_dict.get))
