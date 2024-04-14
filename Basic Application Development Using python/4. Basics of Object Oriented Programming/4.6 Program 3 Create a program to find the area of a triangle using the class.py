# Create a program to find the area of a triangle using the class
class trianglearea:
    def __init__(self, a, b, c):
        import math
        if(a+b)>c and (b+c)>a and (a+c)>b:
            s = (a+b+c)/2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Trangle Area= ",area)
        else:
            print("Trangle is not possible")
a = float(input("Enter First Arm = "))
b = float(input("Enter Second Arm = "))
c = float(input("Enter Third Arm = "))
tarea = trianglearea(a, b, c)
