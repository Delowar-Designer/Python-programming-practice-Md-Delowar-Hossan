# c
my_set = {'Mitu', 'Joty', 'Majdur',1,2,3,4,2.3,True,False,'Mitu'}
print(my_set)
print(type(my_set))
print(len(my_set))

my_set1 = {'Mitu', 'Joty', 'Majdur',1,2,3,4,2.3,True,False,'Mitu'}
for x in my_set1:
    print(x)
print('Mitu' in my_set1)
print('Mitu2' in my_set1)
my_set1.add("Yafta")
print(my_set1)
my_set1.remove("Yafta")
print(my_set1)
my_set1.discard("Mitu")
print(my_set1)
my_set1.pop()
print(my_set1)
my_set1.clear()
print(my_set1)
del my_set1