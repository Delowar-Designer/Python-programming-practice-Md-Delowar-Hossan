#------------------------------------------------------------------------------
#        (+) Mode in Python
#------------------------------------------------------------------------------
file = open("cartoon4.txt","a+")
print(file.read())

file.write("Mitu is a good boy.")
file.seek(0,0)
print(file.read())

file.close()


