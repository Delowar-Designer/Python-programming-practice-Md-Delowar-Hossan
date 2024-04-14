# Inheritance OOP
class Animal:
    def __init__(self, name):
        self.name = name
        print(self.name + "was adopted.")
    def run(self):
        print("running!")
class Dog(Animal):
    def bark(self):
        print("woof!")

# new dog behavior innherited from Animal parent class
spot = Dog("spot") #=> spot was adopted.
spot.run() # => running!

