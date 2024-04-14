# Student class and its three object T S and J
class student:
    def __init__(self, r,n,g):
        self.roll=r
        self.name=n
        self.gpa=g
    def student_info(self):
        print(f'I am {self.name}, my roll and gpa is {self.roll} and {self.gpa}')

T = student(10, 'Mitu',5.00)
S =student(6, 'Joty', 3.3)
J = student(15, 'Delowar', 4.82)
T.student_info()
S.student_info()
J.student_info()