# Program using function to populate content of ffile line by line
with open("app.log","w") as f:
# first line
    f.write("Wow! I am now a python Programmeer.\n")
# Sceond line
    f.write("I am Trained by this book.\n")
# third line
    f.write("This book is published form Haque Publications.")
f.close()
with open("app.log","r") as f:
    print(f.readline())
    print(f.readline())
f.close()

file = open("app.log","r")
for f in file:
    print(f)
file.close()