# For Loop in Python
my_list = ['mitu',1,2,3,4,5,6]
for x in my_list:
    print(x)

name = "Joty"
for x in name:
    print(x)

for x in "Mitu":
    print(x)

for x in "Delowar":
    if (x == "w"):
        continue
    print(x)

print(range(0,10))

x = list(range(0,10))
print(x)

for x in range(0,11,2):
    print(x)
else:
    print("Loop Complete")