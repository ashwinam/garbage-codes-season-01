# Exercise 2: Convert string into a datetime object
from datetime import datetime
'''
For example, You received the following date in string format. Please convert it into Python’s DateTime object.
'''

date_string = "Feb 25 2020 4:20PM"

print(datetime.strptime(date_string, '%b %d %Y %H:%M%p'))