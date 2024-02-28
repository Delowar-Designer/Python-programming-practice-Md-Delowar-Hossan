# 19 Object Oriented Programming (OOP), Class & Object

def method_name(a, b):
    print("A method")

class person:
    def __init__(self, person_name, date_of_birth, ht):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = ht
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if (self. __has_any_namber(new_name)):
            print("Sorry person name can't have number")
            return

        self.name = new_name

    def __has_any_number(self, string):
        return "0" in string

    def get_summary(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"

method_name(10, 20)

a_person = person("Delowar", "2004", "5 feet")
#b_person = person("Mitu")

print(a_person.get_summary())
#print(b_person.get_name())
a_person.set_name("Md Delowar Hossan")
print(a_person.get_summary())
print(a_person.date_of_birth)
a_person.set_neme("0Delowar")
print(a_person.name)