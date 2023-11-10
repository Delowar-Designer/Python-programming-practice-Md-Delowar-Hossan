# তিন বাহুর মান দিয়ে ত্রিভুজের সম্ভাব্যতা যাচাইপূর্বক ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম:

import math
a=int(input("Enter the Value of A="))
b=int(input("Enter the Value of B="))
c=int(input("Enter the Value of C="))
if (a+b)>c and (b+c)>a and (c+a)>b:
    s=(a+b+c)/2
    area= math.sqrt (s*(s-a)*(s-b)*(s-c))
    print(area)
else:
    print("Trangle is not possible")
    
