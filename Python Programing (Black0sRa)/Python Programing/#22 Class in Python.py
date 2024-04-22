# Class in Python
'''class ClassName:
    def myFunction(self):
        print("My Function")
    def yourFunction(self):
        print("Your Function")
classname = ClassName()
classname.p=10
classname.q=20
print(classname.p)
classname.myFunction()
classname.yourFunction()

secondclass = ClassName()
secondclass.p=50
print(secondclass.p)
secondclass.yourFunction()'''

class Person:
    def __init__(D, x, y):
        D.x = x
        D.y = y

    def myFunction(DD):
        print(f"Your name is {DD.x}")
        print(f"Your brathers name is {DD.y}")
    def yourFunction(self):
        pass

classname = Person("Mitu","Joty")
classname.myFunction()