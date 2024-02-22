#63 Python Iterator
list = [1,2,3,4,5,"Delowar","Mitu","joty"]
for i in list:
    print(i)

x = iter(list)
print(x.__next__())
print(next(x))
print(next(x))