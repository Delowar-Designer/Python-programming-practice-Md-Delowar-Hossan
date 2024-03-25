#------------------------------------------------------------------------------
#2     Create, open, Read, Close
#------------------------------------------------------------------------------
open("cartoon2.txt","x")

file = open("cartoon2.txt","r")
print(file.readable())
print(file.readlines())
print(file.readline())
print(file.readline())


print(file.read(10))