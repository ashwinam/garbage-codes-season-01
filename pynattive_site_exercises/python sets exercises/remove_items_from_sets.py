# Exercise 5: Remove items from the set at once

'''
Write a Python program to remove items 10, 20, 30 from the following set at once.
'''

set1 = {10, 20, 30, 40, 50}

for i in [10, 20, 30]:
    set1.discard(i)

print(set1)

# Other solution

set1.difference_update({10, 20, 30})
print(set1)