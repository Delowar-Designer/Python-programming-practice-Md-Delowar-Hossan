#50 Python while and for Loops
delowar = 0
while delowar < 100:
    print("yea Delowar is less then 10",delowar)
    delowar = delowar + 1

fruits = ["apple","banana","cherry"]
for n in fruits:
    print(n)

fruits1 = ["Apple","Banana","Cherry"]
for t in fruits1:
    if t == "Banana":
        break
    print(t,"Braeak iteam")