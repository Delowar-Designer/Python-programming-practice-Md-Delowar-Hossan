#56 Python Lamdda Functions
def DelowarFun(a,b):
    sum = a +b
    print(sum)

x = lambda a,b:a + b
print(x(10, 20))

x = lambda a,b,c,d: (a + b) / (c + d)
print(x(50,35,3,4))