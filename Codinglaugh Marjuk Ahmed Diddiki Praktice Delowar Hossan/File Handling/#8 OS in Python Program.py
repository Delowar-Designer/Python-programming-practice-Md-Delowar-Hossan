#8 OS in Python Program
#------------------------------
import os
os.rmdir("Mitu")

os.rename("Mitu","Delowar")



os.chdir("Mitu")
open("Mitu.txt","x")
os.mkdir("Mitu")

print(os.listdir(os.getcwd()))



print(os.getcwd())
