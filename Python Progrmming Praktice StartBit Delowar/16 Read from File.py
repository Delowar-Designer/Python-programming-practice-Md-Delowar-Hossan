#16 Read from File
f = open('example.txt','r')
print(f.read(10))
print(f.readline())

for x in f:
    print(x)