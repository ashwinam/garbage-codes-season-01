# Exercise 10: Read line number 4 from the following file

'''
open a file 
read from the file
in that file just read the line no 4
'''


with open('file_10.txt') as file:
    for line, content in enumerate(file.readlines(), start=1):
        if line == 4:
            print(content)


# second solution

# read file
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])
