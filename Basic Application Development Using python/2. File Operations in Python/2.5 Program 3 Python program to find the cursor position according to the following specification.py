# Python program to find the cursor position according to the following specification
def program9():
    f = open("info.txt","r")
    print(f.tell())
    f.seek(4,0)
    print(f.read(5))
    f.seek(10,0)
    print(f.tell())
    print(f.read(10))
program9()