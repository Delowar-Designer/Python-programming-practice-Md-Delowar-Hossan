#৭- ফাংশন ব্যবহার করে ত্রিভুজ ক্ষেত্রের ক্ষেত্রফল নির্ণয় করার প্রোগ্রাম।
#7- Program to find the area of a triangle using functions.
import math
def Triangle():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    c = int(input("Enter the value of c:"))
    if((a+b)<c and (b+c)>a and (c+a)>b):
        s = (a+b+c)/2
        Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of the triangle is:",Area)
    else:
        print("The Triangle is not possible")
Triangle()
