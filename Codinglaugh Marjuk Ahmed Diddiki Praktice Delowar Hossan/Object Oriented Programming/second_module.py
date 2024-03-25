from first_module import Human

class Animal(Human):
    def __init__(self, name, age, food, pet):
        super().__init__(name, age, food)
        self.pet = pet
        
    def show_pet(self):
        print(self.pet)