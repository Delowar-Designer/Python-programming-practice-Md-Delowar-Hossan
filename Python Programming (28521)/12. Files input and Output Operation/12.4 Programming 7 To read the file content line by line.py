# To read the file content line by line
file = open("app.log","r")
for f in file:
    print(f)
file.close()