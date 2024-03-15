#------------------------------------------------------------------------------
#       Update, Delete
#--------------------------------------------------------------------------'----
'''file = open("cartoon4.txt","r+")
print(file.read())
file.seek(0,0)
file.write("shinchan")
file.seek(0,0)
print(file.read())
file.close()'''

import os

os.remove("cartoon4.txt")