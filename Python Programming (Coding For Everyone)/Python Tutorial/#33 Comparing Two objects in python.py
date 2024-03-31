#33 Comparing Two objects in python
class Student:
    def __init__(self):
        self.name = 'Mitu'
        self.marks = 85
    def update(self):
        self.name = 'Joty'
        self.marks = 58
    def compare(self,other):
        if self.name==other.name:
            return True
        else:
            return False

Delowar = Student()
sam = Student()
Delowar.update()

if Delowar.compare(sam):
    print("Ther are on")
else:
    print("Ther are off")