#Calculate the difference between two dates using the Time Delta module
from datetime import timedelta
#This represents 1 day.
a=timedelta(days=1)
#Represents 1 hour.
b=timedelta(hours=2)
#Subtract 1 hour from 1 day.
c = a - b
print(c)