# Exercise 1: Print current date and time in Python


from datetime import datetime

print(datetime.now())

# only time
print(datetime.now().time())


# only date
print(datetime.now().date())

from time import gmtime, strftime

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))