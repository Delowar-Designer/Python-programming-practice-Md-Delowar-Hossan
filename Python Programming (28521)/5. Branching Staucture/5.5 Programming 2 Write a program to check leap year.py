# Write a program to check leap year
# Pyghon Program to Check Leap Year using if Statement
year = int(input("Please Enter The Year Number you wish: "))
if ((year% 400 == 0) or ((year%4 == 0) and (year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)