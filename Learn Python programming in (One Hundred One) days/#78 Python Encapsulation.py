#78 Python Encapsulation
class Employee:
    def __init__(self, name, university, salary):
        self.__name = name
        self.university = university
        self.salary = salary
        #print(self.__name)

x1 = Employee("Md Delowar Hossan", "DPI", 222000)
print(x1.name,x1.university,x1.salary)
