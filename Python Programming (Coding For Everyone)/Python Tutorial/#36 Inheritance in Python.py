#36 Inheritance in Python
class A:
    def m1(self):
        print("I am m1")

class B:
    def m2(self):
        print("I am m2")

class C(A,B):
    def m3(self):
        print("I am m3")

a1 = A()
b1 = B()
c1 = C()


print(c1)