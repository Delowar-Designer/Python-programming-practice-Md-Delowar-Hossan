# File reading function
info = open("info.txt","r")
print(info.read(80))
info.close()

fread = open("info.txt","r")
print(fread.read())
fread.close()
