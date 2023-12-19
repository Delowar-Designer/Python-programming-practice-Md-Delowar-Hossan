# List part 2
subjects = ["c","c++","java","python","BASTC"]

print(subjects)
print(len(subjects))

subjects.append("Toc")
print(subjects)

subjects.insert(2,"os")
print(subjects)

subjects.remove("c")
print(subjects)

subjects1 = [20,10,41,47,14,7,8]
print(subjects1)

subjects1.sort()
print(subjects1)

subjects1.reverse()
print(subjects1)

subjects1.pop()
print(subjects1)

subjects2 = subjects1.copy()
print("copy ",subjects2)

index1 = [1,2,6,7,8,3,4,5,4,9]
index = index1.index(4)
print(index)

con = index1.count(4)
print(con)

index1.clear()
print(index1)