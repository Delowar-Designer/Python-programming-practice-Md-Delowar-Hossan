# File Access mode
f = open('file.txt','w')
f.write('Welcame to Programmiar Delowar Hossan')
f.close()


f = open('file.txt','r')
x = f.read()
print(x)
f.close()