# Description of classes and objects with example
class person:
    name = "Mitu"
    sex = "F"
    age = '20'
    def person_info(self):
        print(f'I am {self.name}, {self.age} years old and I am {self.sex}')
p = person()
print(p.name)
p.person_info()
