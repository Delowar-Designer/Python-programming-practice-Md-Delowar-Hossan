# Program to find area of triangle using function
import math
def triagle_area():
    a = float(input("Enter the First Arm = "))
    b = float(input("Enter the Second Arm = "))
    c = float(input("Enter the Third Arm = "))
    if (a + b)>c and (b + c)>a and (a + c)>b:
        s = (a + b + c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("The area Triangle",area)
    else:
        print("The area is Not Possible")
triagle_area()

