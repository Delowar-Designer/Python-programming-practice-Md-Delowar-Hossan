#77 Python Polymorphism
class veicle:
    def __init__(self, Model, Brand, Component,):
        self.Model = Model
        self.Brand = Brand
        self.Component = Component

class Plane(veicle):
    pass

class Car(veicle):
    pass

class Bike(veicle):
    pass

p1 = Plane("Delowar","Delowar.Designer","All Component")
c1 = Car("BMW", "E221", "Main Component")
B1 = Bike("RTR", "E22441", "Main onent")

print(p1.Brand, p1.Model, p1.Component)
print(c1.Model, c1.Brand, c1.Component)
print(B1.Model, B1.Brand, B1.Component)
