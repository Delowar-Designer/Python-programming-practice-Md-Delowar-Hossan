# Abstraction OOP
class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name + "was adopted.")
    def bark(self):
        print("woof!")
# we dontt care how it works just bark
spot = Dog("spot") #=> spot was adopted.
spot.bark() # => woof!
