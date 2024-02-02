# Built-in tuple functions all
tuple =(1,3,4,5)
print(all(tuple))

# all values false
tuple = (0,False)
print(all(tuple))

# one false value
tuple = (1,3,4,0)
print(all(tuple))

# one true value
tuple = (0,False, 5)
print(all(tuple))

# empty iterable
tuple = ()
print(all(tuple))
