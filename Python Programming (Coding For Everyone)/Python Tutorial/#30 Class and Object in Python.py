#30 Class and Object in Python
class Student:
    def name(self):
        print("this is a Student")

rahul = Student()
a = 10
print(type(a))
print(type(rahul))
sam = Student()
Student.name(sam)
Student.name(rahul)
rahul.name()
