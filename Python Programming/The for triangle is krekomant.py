import math
a=int(input("Enter the value of A"))
b=int(input("Enter the value of B"))
c=int(input("Enter the value of C"))
if(a+b)>c and (b+c)>a and (c+a)>b:
    s =(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("the RESULT IS=",area)
else:
    print("triangle is not possible")
    
