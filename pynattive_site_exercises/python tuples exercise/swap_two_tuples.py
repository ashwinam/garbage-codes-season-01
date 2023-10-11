# Exercise 5: Swap two tuples in Python


tuple1 = (11, 22)
tuple2 = (99, 88)

print('--Before--')
print(tuple1)
print(tuple2)

tuple1, tuple2 = tuple2, tuple1

print('--After--')
print(tuple1)
print(tuple2)