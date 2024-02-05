# Yesterday date
from datetime import date
from datetime import timedelta
def yesterday():
    today = date.today()
    yesterday = today-timedelta(days=1)
    return yesterday
print("Todays Date is: ", date.today())
print("Yesterday was:",yesterday())
