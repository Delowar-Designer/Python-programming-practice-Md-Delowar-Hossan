#------------------------------------------------------------------------------
#        Seek Mathod in Python
#------------------------------------------------------------------------------
file = open("cartoon4.txt","r")
file.seek(11,0)
print(file.read(9))

file.seek(0,2)
print(file.read())

file.close()