# Built in list functions and methods all functions
list = [1,2,3,4,5]
print(all(list))
# all values false
list = [0, False]
print(all(list))

# one false value
list = [1,3,4,0]
print(all(list))
# one true value
list = [0,False,5]
print(all(list))
# empty iterable
list = []
print(all(list))
