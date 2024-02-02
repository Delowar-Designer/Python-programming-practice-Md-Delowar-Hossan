# Built-in tuple functions enumearte
grocery = ('bread','milk','butter')
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))

# converting to tuple
print(tuple(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(tuple(enumerateGrocery))

