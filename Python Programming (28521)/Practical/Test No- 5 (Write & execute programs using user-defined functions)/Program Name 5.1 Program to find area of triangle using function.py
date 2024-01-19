# Program to find area of triangle using function
import math
def triagle_area():
    a = float(input("Enter the First value of a: "))
    b = float(input("Enter the Second value of b: "))
    c = float(input("Enter the Third value of c: "))
    if(a+b)>c and (b+c)>a and (a+c)>b:
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Triangle Area= ",area)
    else:
        print("Triangle is not possible")
triagle_area()