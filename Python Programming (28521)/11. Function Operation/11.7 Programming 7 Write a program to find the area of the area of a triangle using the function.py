# Write a program to find the area of the area of a triangle using the function
import math
def Triangle():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    if((a+b)<c and (b+c)>a and (c+a)>b):
        s = (a + b + c)/2
        Area = math.sqrt(s* (s-a)*(s-b)*(s-c))
        print("Area of the triangle is: ",Area)
    else:
        print("The triangle is not possible")
Triangle()