#64 Python Scope
a = 34 # global varieabole
b = 23

def sum():
    global a
    x = 100 # Local scope varieabole
    print(x)
    print(a)
sum()