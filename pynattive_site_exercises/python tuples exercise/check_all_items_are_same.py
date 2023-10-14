# Exercise 10: Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 55)

val = tuple1[0]

flag = False

for i in tuple1:
    if i == val:
        flag = True
    else:
        flag = False
        break

if flag:
    print('All items are same in the tuple.')
else:
    print('All items in the tuple are not same.')