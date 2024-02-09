# Write a Program to solve quadratic equation in python using class
import math
class equation:
    def quardatic(selfself,a,b,c):
        d = b * b - 4 * a * c
        if d > 0:
            print("real and different roots")
            print((-b + math.sqrt(d))/(2*a))
            print((-b - math.sqrt(d))/(2*a))
        elif d == 0:
            print("real and same roots")
            print(-b/(2*a))
        else:
            print("Complex Roots")

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
x = equation()
x.quardatic(a,b,c)