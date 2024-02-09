# Write a Program of single inheritance in python
class math:
    def add(selfself,x,y):
        return x+y
class inheritance(math):
    def sub(selfself,x,y):
        return x-y
p = inheritance()
a = p.add(3,4)
print("x+y=",a)
b = p.sub(20,10)
print("x-y=",b)

