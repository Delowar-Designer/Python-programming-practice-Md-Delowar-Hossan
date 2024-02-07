# To read the file content line by line
with open("app.log","w")as f:
    # first line
    f.write("Wow! i'm now a python programmer.\n")
    # secnd line
    f.write("I am trained by this book.\n")
    # thir line
    f.write("This book is published from Haque Publications.")
f.close()
with open("app.log","r")as f:
    print(f.readline())
    print(f.readline())
f.close()
