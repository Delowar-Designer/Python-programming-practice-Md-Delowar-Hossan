# Create programs to find roots of quadratic equations using classes
class QuadraticEq:
    def __init__(self,a,b,c):
        import math
        d = (b*b)-(4*a*c)
        if(d<0):
            print("Roots are imaginary")
        else:
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            print("X1 = %.2f"%x1,"X2 = %.2f"%x2)
            print("Roots are Real")

a = int(input("A = ?"))
b = int(input("B = ?"))
c = int(input("C = ?"))
qrdeq = QuadraticEq(a,b,c)
