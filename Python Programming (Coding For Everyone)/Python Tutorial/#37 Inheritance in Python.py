#37 Inheritance in Python
class A:

    def __init__(self):
        print("i an in A Init")
    def m1(self):
        print("I am a")
class B:
    def __init__(self):
        print("I am b Init")

    def m2(self):
        print("I am B")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("i am in c Init")
    def m3(self):
        print("I am in m3 c")

c1 = C()
