#------------------------------------------------------------------------------
#        Append, Write, Clase
#------------------------------------------------------------------------------
file = open("cartoon4.txt","a")

file.write("Programmer Delowar.Designer")
file.write("Programmer2\nDeveloper2\nDesigner")
file.close()

file_r = open("cartoon4.txt","r")

print(file_r.read())
file_r.close()