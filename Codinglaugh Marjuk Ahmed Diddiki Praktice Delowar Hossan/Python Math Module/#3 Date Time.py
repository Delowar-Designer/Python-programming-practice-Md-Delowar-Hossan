# Date Time
#import datetime
from datetime import date, time, datetime, timedelta
import time as t
#print(datetime.date.today())

print(date(2024,11,6))

x = date(2023,11,4)
print(x.month)
print(x.year)
print(x.day)

print(time(12,23,43,13))

t = time(12,23,43,13)
print(t.microsecond)
print(t.tzinfo)

print(datetime.now().minute)



#birth_d = datetime(2024,1,1)
#print(birth_d.datetime.today())

#print(t.time)
#print(datetime.fromtimestamp(t.time()))


d = datetime.now()
print(d.minute)
print(d + timedelta(minutes=30))

