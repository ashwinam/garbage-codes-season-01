# Exercise 8: Update set1 by adding items from set2, except common items

import pprint


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()

if set1.isdisjoint(set2):
    print('No common elements is available.')
else:
    pprint.pprint(set1.symmetric_difference(set2))