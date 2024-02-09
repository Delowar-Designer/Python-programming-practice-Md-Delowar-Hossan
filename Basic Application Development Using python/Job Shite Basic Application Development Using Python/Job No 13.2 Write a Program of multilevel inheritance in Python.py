# Write a Program of multilevel inheritance in Python
class math:
     def add(self,x,y):
         return x+y
class inheritance(math):
    def sub(self,x,y):
        return x-y
class dpi(inheritance):
    def multi(self,x,y):
        return (x*y)
p = dpi()
a = p.add(3,4)
print("x+y=",a)
b = p.sub(20,10)
print("x-y=",b)
c = p.multi(5,6)
print("x*Y=",c)