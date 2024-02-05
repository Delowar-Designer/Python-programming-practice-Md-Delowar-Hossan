# Tomorrow date
from datetime import date
from datetime import timedelta
def tomorrew():
    return date.today()+timedelta(days=1)
print("Todays Date is :",date.today())
print("Tomorrow Date will be :",tomorrew())
