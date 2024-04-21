# For Loop
for i in 'Programming':
    print(i)

i = 1
while (i<=10):
    print(i)
    i = i+1

for i in range(0,10,3):
    print(i)

for i in range(0,101):
    if i % 2 == 0:
        print(i)

for name in ['dog','cat','elephant']:
    new_line = "I Love "
    print(new_line + name.upper())

print("*" * 5)

for i in range(1,6):
    print("#"*i)

for i in range(6,0,-1):
    print("#"*i)

for x in range(1,6):
    for y in range(1,6):
        print(f'({x}, {y})')