# A program to find the area of a triangle with the values of three sides
import math
a = int(input("Enter the Value of a: "))
b = int(input("Enter the Value of b: "))
c = int(input("Enter the Value of c: "))
if (a+b)>c and (a+c)>c and (c+a)>b:
    s = (a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(Area)
else:
    print("Triangle is not possible")
