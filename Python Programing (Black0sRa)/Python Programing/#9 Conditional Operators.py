# Conditional Operators
a = 10
b = 5

if(a>b):
    print('Yes it is a valid condition')

print("Finishe our conditio")

if(20 != 5):
    print('Yes it is a valid condition')
else:
    print("No, it is not valud")

print("Finishe our conditio")


age = int(input('What is yout age: '))

if (age >= 18):
    print("You can vote")
else:
    print("No you cant vote")

if (age>=1 and age<13):
    print("Child")
elif(age>=13 and age <20):
    print("Teenager")
elif(age>=20 and age<41):
    print('young')
else:
    print("old")
