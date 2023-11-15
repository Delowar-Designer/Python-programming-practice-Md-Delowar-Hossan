#---- FILE in Python ---

# python File Handlig


# creating a new file 
'''
f = open("demo.txt","x")

# writtig a file
f = open("demo.txt","W")
#f.write("I Love Allha")

# append/add a new line
f = open("demo.txt","a")
#f.write("and Al Quran")
#f.write("\nI Love Allha and Al Quran")
#f.write("\nI Love Allha and Al Quran")
# File wittig
f = open("demo.txt","r")
x = f.read()
print(x)

#one Line reade
f = open("demo.txt","r")
first_line = f.readline()
print(first_line)
second_line = f.readline()
print(second_line)
f.close()

# delete a file
import os
#f = open("demo.txt","r")
os.remove("demo.txt")
f.close()


# existing file oppen
f = open(r"C:\Users\Delowar2004\Desktop\New.txt","r")
x = f.read()
print(x)
f.close()
'''

# existing file line line oppen
f = open(r"C:\Users\Delowar2004\Desktop\New.txt","r")
x1 = f.readline()
x2 = f.readline()
x3 = f.readline()
print(x1)
print(x2)
print(x3)
f.close()
