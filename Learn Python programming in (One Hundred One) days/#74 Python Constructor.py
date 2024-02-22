#74 Python Constructor


# Parameterized Constructot
class MyClass:
    def DelowarFamily(self, name, age):
        print(f"my name is {name},my age is {age}")

p1  = MyClass()

p1.DelowarFamily("Mitu",21)
p1.DelowarFamily("Joty",26)
p1.DelowarFamily("Delowar",19)


class parentInfo:
    def __init__(self,Name, Number):
        print(f"My Name is {Name}, & My Numbers is {Number}")

p2 = parentInfo("Delowar","0177387009038")
p2 = parentInfo("Mitu","019038")