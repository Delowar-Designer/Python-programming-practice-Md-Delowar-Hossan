a=int(input("Enter the number of A="))
b=int(input("Enter the number of B"))
c=int(input("Enter the number of C"))
if a>b and b>c:
    print ("largest value is A=",a)
elif b>a and b>c:
    print("largest value is B=",b)
else:
    print ("largest value is c=",c)
