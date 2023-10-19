# Exercise 6: Add a week (7 days) and 12 hours to a given date

from datetime import datetime, timedelta

# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)


print(given_date + timedelta(days=7, hours=12))
