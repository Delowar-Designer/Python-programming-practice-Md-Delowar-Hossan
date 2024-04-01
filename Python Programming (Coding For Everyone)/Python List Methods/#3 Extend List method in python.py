#3 Extend List method in python
lst =  [1,2,3,4,5,6,7,8,9]

lst1 = [10,45,78]
lst[len(lst):]=lst1
print(lst)
print(len(lst))

print(lst.extend(lst1))
lst = lst+lst1
print(lst)