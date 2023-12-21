# xargs & xxargs
def student (id,name):
    print(id,name)

student(123,"Delowar")

def student (*details):
    print(details)

student(123,"Delowar",4.82)

def add(num1,num2):
    sum = num1 + num2
    print(sum)

add(10,20)

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
add(44,47,4)
add(8,3,5,2,6)

# xxargs
def student(id,name):
    print(id,name)

student(id=1213,name="Md Delowar Hossan")


def student(**details):
    print(details)
    print(details["name"])

student(id=1213, name="Md Delowar Hossan")