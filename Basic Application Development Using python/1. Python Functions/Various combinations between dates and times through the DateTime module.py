#The Function Various combinations between dates and times through the DateTime module1
import datetime
n=datetime.datetime.now()
t=datetime.datetime.today()
u=datetime.datetime.utcnow()
print("Now:",n)
print("Today:",t)
print("UTC now:",u)


#The Various combinations between dates and times through the DateTime module2
import datetime
t=datetime.time(12,46,30)
print("Time is:",t)
d=datetime.date.today()
print("Date is:",d)
dt=datetime.datetime.combine(d,t)
print("Date & Time is:",dt)
