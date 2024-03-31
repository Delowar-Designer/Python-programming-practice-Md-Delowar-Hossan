#31 ___init__ method in python
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        #print("I am from Init")

    def details(self):
        print("Name:",self.name)
        print("Roll:",self.roll)

Rahul = Student("Rahul",58)
sam = Student("Sam", 47)
Rahul.details()
sam.details()
