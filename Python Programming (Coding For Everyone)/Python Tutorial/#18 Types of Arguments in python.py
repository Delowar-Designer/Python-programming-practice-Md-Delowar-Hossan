#18 Types of Arguments in python
def my_func(a,b,c):
    print(a)
    print(b)
    print(c)
    d = a+b+c
    print(d)
my_func(54, 7, 8)

def student(name,roll):
    print(name)
    print(roll)
student("Mitu",45)

def student(name,roll=0):
    print(name)
    print(roll)
student(name="Delowar")

def add(*b):
    print(b)
    c=0
    for i in b:
        c=c+i
    print(c)
add(2,3,3)