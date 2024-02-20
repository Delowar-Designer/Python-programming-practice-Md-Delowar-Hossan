#31 Python Update Tuples
ThisTuple = ("Hello", "World", "Delowar","Mitu")
a = list(ThisTuple)
a.append("Joty")
print(ThisTuple)
print(a)

ThisTuple = tuple(a)
print(ThisTuple)

a[1] = "Majdur"
ThisTuple = tuple(a)
print(ThisTuple)