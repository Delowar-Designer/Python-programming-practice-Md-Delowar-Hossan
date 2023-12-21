# Constructor
class student:
    name = ""
    roll = ""
    gpa = ""

    def __init__(self, name, roll, gpa):
        self.name = name
        self.roll =roll
        self.gpa = gpa
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, GPA: {self.gpa}")


Delowar = student("Delowar Hossan", 60,4.00)
Delowar.display()


Mitu = student("Mitu Hsaoune",122,3.45)
Mitu.display()

