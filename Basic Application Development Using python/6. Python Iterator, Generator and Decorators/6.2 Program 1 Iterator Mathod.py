# Iterator Mathod
a = [0, 5, 10, 15, 20]
for i in a:
    if i % 2 == 0:
        print(str(i)+' is an Even Number')
    else:
        print(str(i)+' is an Odd Number')

b = iter([0, 5, 10, 15, 20])
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))