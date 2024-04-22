# Exception Hanndling
'''try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")'''
'''
try:
    name = int(input("> "))
    print(name)
    age = 21
    day = age/0
    print(age)
except Exception:
    print("You cant Exception")
finally:
    print("I am final Code")
except ZeroDivisionError:
    print("You cant divide age by 0")
except ValueError:
    print("Invalid value")'''


age = -1

if age < 0:
    raise Exception("Your age cant under 0")


