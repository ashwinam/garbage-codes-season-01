# Exercise 7: Print current time in milliseconds
from datetime import datetime

print(datetime.now().timestamp())

# Other solution
import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)
