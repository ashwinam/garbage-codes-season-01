# Exercise 6: Write all content of a given file into a new file by skipping line number 5

'''
1. create a file and insert a content there
2. read the file and start appending it another file 
    i. but except line 5

'''


with open('test_6.txt', 'r') as file1:
    for line, content in enumerate(file1.readlines(), start=1):
        if line == 5:
            continue
        with open('test_6_1.txt', 'a') as file2:
            print(' i a here')
            file2.write(content)
