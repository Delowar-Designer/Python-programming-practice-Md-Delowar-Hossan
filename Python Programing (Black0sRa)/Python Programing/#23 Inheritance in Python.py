# Inheritance in Python
class Animal:
    def walk(self):
        print("I can walk")
class Dog(Animal):
    def run(self):
        print("I can ran")

class Cat(Animal):
    pass

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()
dog = Dog()
dog.run()

