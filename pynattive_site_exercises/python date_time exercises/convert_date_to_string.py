# Exercise 8: Convert the following datetime into a string

from datetime import datetime


given_date = datetime(2020, 2, 25)

print(str(given_date))


# Other solution
from datetime import datetime

given_date = datetime(2020, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)
