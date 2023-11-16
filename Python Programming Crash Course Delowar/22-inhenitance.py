#---- Inheritance in Python ---

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print(self.name + " walks")

#a=Animal("Puppy")
#a.walk()

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    def sound(self):
        print(self.name + " barks")

x = Dog("Coco",1)
y = Dog("ALSA",1)
x.walk()
x.sound()
y.walk()
y.sound()

