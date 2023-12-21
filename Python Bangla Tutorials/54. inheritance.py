# Inheritance
# parent class, super class, Base class
# Child class, sub class, Derived class
class phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

class samsung(phone):
    '''def call(self):
        print("You can call")

    def message(self):
        print("You can message")'''
    # Call , message
    def photo(self):
        print("You can take photo")

p = phone()
p.message()
p.call()

s = samsung()
s.message()
s.call()
s.photo()

print(issubclass(samsung,phone))
print(issubclass(phone,samsung))