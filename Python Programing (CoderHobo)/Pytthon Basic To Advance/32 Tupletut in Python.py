# Tupletut in Python
my_tuple = ('Mitu','joty',3,4,5,6)
print(type(my_tuple))
print(my_tuple[-1])

# tupletut slising
my_tuple1 = (2,3,4,5,6,7,8)
print(my_tuple1[2:5])

# tup Updede
my_tuuple = (2,3,46)
x = list(my_tuuple)
print(type(x))
x[2] = 10
print(x)
y = tuple(x)
print(y)

mytuple2 = (2,3,45,67,)
y   = (34,56)
mytuple2 += y
print(mytuple2)
x = list(mytuple2)
x.remove(3)
z = tuple(x)
print(z)
