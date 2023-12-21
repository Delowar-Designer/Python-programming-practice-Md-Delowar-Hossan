# Readin a File
file = open("student.txt","r+")
#print(file.writable())
#text = file.read()
#print(text)

#size = len(text)
#print(size)

#read = file.readlines()[1]
#print(read)

for line in file:
    print(line)
    
file.close()