# Break and continue
i = 1
while i <= 100:
    if i == 20:
        break
    print(i)
    i = i + 1
print("Goodbye")

a = 1
while a <= 10:
    print(a)
    a = a + 1
    if a == 5:
        break
print("Bye")

t = 1
while t <= 100:
    if t == 20:
        continue
    print(t)
    t = t + 1
print("Goodbye Continue")

b = 1
while b <= 10:
    print(b)
    b = b + 1
    if b == 5:
        continue
print("Bye Continue")