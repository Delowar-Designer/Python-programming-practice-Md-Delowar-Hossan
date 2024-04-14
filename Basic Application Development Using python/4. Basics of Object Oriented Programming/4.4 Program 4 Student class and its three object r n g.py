# Student class and its three object r n g
class student:
    def __init__(self,r,n,g):
        self.roll = r
        self.name = n
        self.gpa = g

    def student_info(self):
        print(f'I am {self.name}, my roll and gpa is {self.roll} and {self.gpa}')

T = student(10, "Mitu", 3.5)
S = student(120, "Joty", 4.5)
J = student(20, "Yafta", 4.14)

T.student_info()
S.student_info()
J.student_info()
T.address = 'Delowar'
print(f'I am {T.name}, my roll and gpa is {T.roll} and {T.gpa} also address is : {T.address}')
