# Exercise 4: Print a date in a the following format
from datetime import datetime
'''
Day_name  Day_number  Month_name  Year
'''

given_date = datetime(2020, 2, 25)

print(given_date.strftime('%A %d %B %Y'))


