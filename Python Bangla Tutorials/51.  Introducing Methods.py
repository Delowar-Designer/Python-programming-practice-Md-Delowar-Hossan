# introducing Methods
class student:
    name = ""
    roll = ""
    gpa = ""

    def set_value(self, name, roll, gpa):
        self.name = name
        self.roll =roll
        self.gpa = gpa
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, GPA: {self.gpa}")

Delowar = student()
Delowar.name = "Md Delowar Hossan"
Delowar.roll = 602826
Delowar.gpa = 4.82
Delowar.display()
Delowar.set_value("Delowar Hossan", 60,4.00)
Delowar.display()

Mitu = student()
Mitu.name = "Ms Mitu Hsaoune"
Mitu.roll = 602827
Mitu.gpa = 5.00
Mitu.display()
Mitu.set_value("Mitu Hsaoune",122,3.45)
Mitu.display()

# introducing Methods
'''class student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

Delowar = student()
Delowar.set_value(60,4.00)
Delowar.display()

Mitu = student()
Mitu.set_value(122,3.45)
Mitu.display()'''

