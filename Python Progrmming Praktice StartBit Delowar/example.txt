#14 Nested List and Built in List Functions
list1 = [["A", ["Mitu","Joty"],"B", "C"],1,2,3,4,5,6,7,8,"Delowar"]
print(list1)
print(list1[0][1][1])

list = ["A",1,2,3,4,5,6,7,8,2,2]
print(list.index("A"))
print(list.count(2))
list.append(33)
list.insert(2,30)
list.extend([23,45,1, 5,6,7])
list = list + [50,60,70]
list.remove("A")
list.pop()
list.remove(list[1])
list.sort()
print(list)