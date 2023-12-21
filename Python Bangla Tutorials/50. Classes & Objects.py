# Classes & Objects
class student:
    name = ""
    roll = ""
    gpa = ""

Delowar = student()
print(isinstance(Delowar,student))

Delowar.name = "Md Delowar Hossan"
Delowar.roll = 602826
Delowar.gpa = 4.82
print(f"Name: {Delowar.name}, Roll: {Delowar.roll}, GPA: {Delowar.gpa}")


Mitu = student()
Mitu.name = "Ms Mitu Hsaoune"
Mitu.roll = 602827
Mitu.gpa = 5.00
print(f"Name: {Mitu.name}, Roll: {Mitu.roll}, GPA: {Mitu.gpa}")

