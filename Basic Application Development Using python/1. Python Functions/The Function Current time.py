#The Function Current time
import time
localtime=time.localtime(time.time())
print("local current time is:",localtime)


# The Function current Date
from datetime import time
from datetime import date
from datetime import datetime
today=date.today()
print("Current Date is :",today)


#The Function Yesterday date
from datetime import date
from datetime import timedelta
def Yesterday():
    today=date.today()
    Yesterday=today-timedelta(days=1)
    return Yesterday
print("Todays Date is :", date.today())
print("Yesterday was :",Yesterday())


#The Function Tomorrow date
from datetime import date
from datetime import timedelta
def tomorrow():
    return date.today()+timedelta(days=1)
print("Todays Date is :",date.today())
print("Tomorrow Date Will be :",tomorrow())

# The Function Find today's date and time
from datetime import time
from datetime import date
from datetime import datetime
today=datetime.today()
print("Todays Date & Time is :",today)
