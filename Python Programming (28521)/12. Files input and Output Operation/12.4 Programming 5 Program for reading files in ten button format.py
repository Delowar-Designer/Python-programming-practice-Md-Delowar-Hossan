# Program for reading files in ten button format
fread = open("info.txt","r")
for_one_char = fread.read(2)
print(for_one_char)
remaining_four_char = fread.read(4)
print(remaining_four_char)
rest_of_the_file = fread.read()
print(rest_of_the_file)
fread.close()