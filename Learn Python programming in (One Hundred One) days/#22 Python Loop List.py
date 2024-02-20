#22 Python Loop List
# You can Loop through the list items by using a for loop::
LoopList = ["Mitu","Jutiy","Yafta","Roby","Majdur"]
for Myfarand in LoopList:
    print(Myfarand)


print('use the range() and len() functions to create a suitable iterable.')
for i in range(len(LoopList)):
    print(i)

print('print all items, using a while loop to go through all the index numbers')
D = 0
while D < len(LoopList):
    print(LoopList[D])
    D = D + 1