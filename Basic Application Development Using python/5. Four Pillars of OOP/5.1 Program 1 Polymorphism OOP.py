# Polymorphism OOP
class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name + "was adopted.")
    def run(self):
        print("running!")
class Turtle(Animal):
    # def __init__(self):
    # super().init
    def run(self):
        print("running slowly!")
# we get back an interesting response
tim = Turtle("tim") # => tim was adopted.
tim.run() # => running slowly!
