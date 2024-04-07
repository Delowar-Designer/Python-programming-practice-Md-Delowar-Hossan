# 2.3 Program 1 File opening and closing functions
'''f = open('file.txt','w')
f.write('Welcome to Python Programming Language')
f.close()'''

f = open('file.txt','r')
x = f.read()
print(x)
f.close()

'''try:
    with open('file.txt', 'r') as f:
        x = f.read()
        print(x)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")'''

my_file = open('test.txt','w')
my_file.write('Welcome to Python Progrramming Language')
my_file.close()
