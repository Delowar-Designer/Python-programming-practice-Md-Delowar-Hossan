#34 Types of variables in Python
class Student:
    school = "ABC school"
    def __init__(self):
        self.name = 'Mitu'
        self.roll = 15

Joty = Student()
Majdur = Student()
Joty.name = 'Delowar'
Joty.school = 'Programing school'
print(Joty.name,Joty.roll,Joty.school)
print(Majdur.name,Majdur.roll,Majdur.school)