# Write a Program to use try and except in python
x = 8
y = 6
try:
    if x<0 or y<0:
        raise ZeroDivisionError
    print(x/y)
except ZeroDivisionError:
    print("Plz give valid number")

