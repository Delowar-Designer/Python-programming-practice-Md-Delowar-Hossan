#18 Context Manager File Handling
'''f = open('example.txt','r')
print(f.read())
f.close()'''

with open('example.txt','r') as f:
    #print(f.read())
    # for x in f:
    #     print(x)
    print(f.read(10))
    print(f.read(10))
