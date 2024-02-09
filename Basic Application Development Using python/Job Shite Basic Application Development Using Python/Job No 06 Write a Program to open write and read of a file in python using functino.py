# Write a Program to open write and read of a file in python using functino
def program():
    f = open("cst.txt","w")
    a = input("Enter the 1st text: ")
    f.write(a)
    f.close()
    f = open("cst.txt","r")
    x = f.read()
    print(x)
    f.close()
program()
