# Time delta module
from datetime import timedelta
# This represents 1 day.
a = timedelta(days=1)
# Represents 1 hours
b = timedelta(hours = 1)
#Subtract 1 Hour from 1 day
c = a - b
print(c)