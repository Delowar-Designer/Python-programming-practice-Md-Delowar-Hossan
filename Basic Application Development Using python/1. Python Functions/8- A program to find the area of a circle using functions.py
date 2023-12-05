#৮- ফাংশন ব্যবহার করে বৃত্তের ক্ষেত্রফল নির্ণয়ের একটি প্রোগ্রাম।
#8- A program to find the area of a circle using functions.
import math
def calculate_area(radius):
    myarea = math.pi*radius**2
    return myarea
radius=calculate_area(int(input("Please input the radius:")))
print("The area of circle is:",radius)
