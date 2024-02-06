# Create a program to find the area of the square using functions
import math
def calculate_area(radius):
    myarea = math.pi*radius**2
    return myarea
radius = calculate_area(int(input("Please input the radius:")))
print("The area of circle is:",radius)
