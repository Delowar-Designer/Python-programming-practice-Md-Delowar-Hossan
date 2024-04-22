# Packages in Python
'''import calendar
print(calendar.calendar(2020))
print(calendar.calendar(2021))
print(calendar.calendar(2022))'''

import random
import math
number = random.random() * 100
result = math.floor(number)
print(result)

print(math.floor(random.random()*10))
for i in range(3):
    print(random.randint(1,200))

name = ["Mitu", "Joty", "Simai"]
print(random.choice(name))