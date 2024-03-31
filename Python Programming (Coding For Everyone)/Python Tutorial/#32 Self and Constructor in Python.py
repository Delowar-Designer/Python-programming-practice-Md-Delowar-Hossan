#32 Self and Constructor in Python
class Student:
    def __init__(self):
        self.name ="rishi"
        self.roll=35
    def update(self):
        self.name = "Mitu"
        self.roll = 56

rahul = Student()
sam = Student()

#rahul.name = "rahul"
#rahul.roll = 25
rahul.update()
print(rahul.name)
print(rahul.roll)
print(sam.name)