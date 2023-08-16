# Exercise 9: Check file is empty or not

with open('file_9.txt') as file:
    content = file.read()
    if content:
        print('file is not empty')
    else:
        print('File is empty.')


# solution using os module

import os

size = os.stat("file_9.txt").st_size
if size == 0:
    print('file is empty')
