# Exercise 10: Calculate number of days between two given dates
from datetime import datetime


# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)



print((date_2.date() - date_1.date()).days, 'days')