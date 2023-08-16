# Exercise 9: Check file is empty or not

with open('file_9.txt') as file:
    content = file.read()
    if content:
        print('file is not empty')
    else:
        print('File is empty.')
