#  Calendar Module
import calendar


for i in calendar.day_name:
    print(i)
    
print(calendar.day_name[6])

for i in calendar.day_abbr:
    print(i)

for i in calendar.month_name:
    print(i)

print(calendar.month_name[1])

print(calendar.calendar(2022))

print(calendar.month(2024, 3))

print(calendar.weekday(2024, 1, 3))

print(calendar.day_name[calendar.weekday(2024, 1, 3)])

print(calendar.isleap(2024))

print(calendar.leapdays(2020, 2030))

cal = calendar.Calendar()

for i in cal.iterweekdays():
    print(i)

cal1 = calendar.Calendar(firstweekday=3)
for i in cal1.iterweekdays():
    print(i)
    
cal2 = calendar.Calendar(firstweekday=0)
for i in cal2.itermonthdays(2022, 10):
    print(i)

for i in cal2.itermonthdays2(2022, 10):
    print(i)
    
for i in cal2.itermonthdays3(2022, 10):
    print(i)

for i in cal2.itermonthdays4(2022, 10):
    print(i)
    
for i in cal2.itermonthdates(2022, 10):
    print(i)
    
for i in cal.monthdatescalendar(2024, 10):
    print(i)
    
for i in cal.monthdayscalendar(2024, 10):
    print(i)
    
for i in cal.monthdays2calendar(2024, 10):
    print(i)

for i in cal.yeardayscalendar(2024, 10):
    print(i)
    
for i in cal.yeardays2calendar(2024, 10):
    print(i)
    
cal4 = calendar.TextCalendar(firstweekday=6)

print(cal4.formatyear(2024))

cla6 = calendar.HTMLCalendar(firstweekday=6)

print(cla6.formatmonth(2024, 10))

print("Year format 2024", cla6.formatyear(2024))