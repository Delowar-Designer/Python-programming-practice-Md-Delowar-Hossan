# Program Name 8.1 Writing data to a file open with append mode)
f = open("demofile2.txt","a")
f.write("Hello Now the file has more content!")
f.write("\nMy Name is Delowar Hossan and I love Python")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt","r")
print(f.read())
f.close()
