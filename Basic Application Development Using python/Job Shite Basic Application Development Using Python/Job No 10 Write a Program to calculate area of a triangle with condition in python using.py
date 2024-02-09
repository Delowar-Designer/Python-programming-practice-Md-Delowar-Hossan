# Write a Program to calculate area of a triangle with condition in python using
import math
def triangle():
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))
    if(a+b>c and b+c>a and c+a>b):
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("The area of the triangle is = ",area)
    else:
        print("Triangle is not Possiable")
triangle()
