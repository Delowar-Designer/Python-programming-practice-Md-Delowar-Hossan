#      Time Module
import time

print(time.time())
print(time.time()*1000)
print(time.time_ns())
print(time.gmtime())
print(time.gmtime(0))
print(time.localtime())
print(time.ctime())
print(time.asctime())
print(time.ctime())
print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime()))
print(time.ctime())
time.sleep(5)
print(time.ctime())
print(time.mktime((2024,10,20,22,13,33,2,293,0)))
print(time.ctime(time.mktime((2024,10,20,22,13,33,2,293,0))))
print(time.strftime("%a %b"))
print(time.strftime("%Y %B %A"))

print(time.strptime("27 september 2024","%d %B %Y"))


