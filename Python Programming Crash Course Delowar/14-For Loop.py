#---- for Loop in python ----
'''
    for variable in sequence:
        statement
'''
# Looping through a list using for loop
my_frined = ["Mitu","Jyoti","Majidur"]
for friend in my_frined:
    # for Loop body
    print(friend)

# Looping through a string using for loop
my_name = "Delowar"
for string in my_name:
    print(string)

# the range (function)
for x in range(10):
    print(x)
    print("Hello Delowar")
# nested for Loop
animal = ["tiger","cat","dog"]
sound = ["roars","meow","barks"]

for x in animal:
    #body of x for loop
    for y in sound:
        # body of nested y for loop
        print("The " + x + " " + y)
