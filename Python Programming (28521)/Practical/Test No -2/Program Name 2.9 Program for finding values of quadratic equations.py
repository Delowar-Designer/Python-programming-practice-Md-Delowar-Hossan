# Program for finding values of quadratic equations
import math
def quadratic():
    a=int(input("Enter the value of A = "))
    b=int(input("Enter the value of B = "))
    c=int(input("Enter the value of C = "))

    d=(b*b)-(4*a*c)
    if (d<0):
        print("The Roots are imaginary")

    else:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b+math.sqrt(d))/(2*a)
        print("X1=%.2f"%x1,"X2=%.2f"%x2)
print("Roots are Real")
quadratic()

