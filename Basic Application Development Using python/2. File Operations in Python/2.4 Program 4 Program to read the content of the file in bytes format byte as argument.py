# Program to read the content of the file in bytes format byte as argument
fread = open("info.txt","r")
for_one_char = fread.read(1)
print(for_one_char)
remainig_four_char = fread.read(4)
print(remainig_four_char)
rest_of_the_file = fread.read()
print(rest_of_the_file)
fread.close()