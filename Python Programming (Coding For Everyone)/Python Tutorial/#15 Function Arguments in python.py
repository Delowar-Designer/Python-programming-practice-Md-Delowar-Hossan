#15 Function Arguments in python
def change(x):
    print(id(x))
    x = 10
    print(id(x))
    print(x)

a = 2
print(id(a))
change(a)

def change(lst):
    print(id(lst))
    lst[1] = 10
    print(id(lst))
    print(lst)

lst = [1,2,3,4]
print(id(lst))
change(lst)

