#20 Global Keyward Local Vaariable in python
a = 10
def nothing():
    a = 17
    print(globals())

nothing()
print(a)