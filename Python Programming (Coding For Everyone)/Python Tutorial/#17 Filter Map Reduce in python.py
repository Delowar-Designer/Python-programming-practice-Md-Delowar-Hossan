#17 Filter Map Reduce in python
l1 = [1,2,3,4,5,6,7,8,9]
new_list = []
for i in l1:
    if i%2!=0:
        print(i)
        new_list.append(i)
print(new_list)

print(list(filter(lambda x:(x%2)!=0,[1,2,3,4,5,6,7,8,9])))

list1 = [1,2,3,4,5,6,7,8,9]

a = lambda x:x*x
print(list(map(a,list1)))


from functools import reduce
l1 = [1,2,3,4,5]
sum=reduce(lambda x,y:x+y,l1)
print(sum)

