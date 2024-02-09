# Write a Program of Polymorphism in python
class math:
    def add(self,x,y):
        return x+y
    def action(self,x,y):
        return x*y
class inheritance(math):
    def action(self,x,y):
        return x+y
p = inheritance()
a = p.add(3,4)
print("x+y=",a)
b = p.action(20,10)
print("x-y=",b)