# Program Name 8.2 Reading data from a FlLE open with append mode
f = open("demofile3.txt","a")
f.write("Hello the file has more content Now")
f.close()

# open and read the file after the appending:
f = open("demofile3.txt","r")
print(f.read())