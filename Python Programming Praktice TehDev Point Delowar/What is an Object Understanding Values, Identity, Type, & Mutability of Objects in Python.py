# What is an Object? Understanding Values, Identity, Type, & Mutability of Objects in Python
age = 30
name = "Delowar"
print(age, name)
print(id(age), id(name))
print(type(age), type(name))
# integer is an immutable object
age = 34
name = "Mitu"
print(age, name)
print(id(age), id(name))
print(type(age), type(name))

list = [1, 2, "Joty"]
print(list)
print(id(list))
print(type(list))
list[2] = "five"
print(list)
print(id(list))
print(type(list))