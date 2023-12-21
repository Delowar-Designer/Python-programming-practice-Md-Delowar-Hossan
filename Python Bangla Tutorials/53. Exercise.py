# Exercise
class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("The area of the triangle is", area)

ti = Triangle(10, 20)
ti.calculate_area()

t2 = Triangle(20, 30)
t2.calculate_area()


