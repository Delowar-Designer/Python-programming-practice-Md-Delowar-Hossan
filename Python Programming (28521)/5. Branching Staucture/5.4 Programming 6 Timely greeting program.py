# Timely greeting program
x = int (input("What is the time: "))
if x < 10:
    print("Godd morning")
elif x < 12:
    print("Soon time for lunch")
elif x < 18:
    print("Good day")
elif x < 22:
    print("Bood evening")
else:
    print("Good night")