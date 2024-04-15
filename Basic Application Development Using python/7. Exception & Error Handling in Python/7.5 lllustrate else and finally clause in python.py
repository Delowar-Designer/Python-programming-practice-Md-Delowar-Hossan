# lllustrate else and finally clause in python
def divide(x, y):
    try:
        result = x//y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero")
    else:
        print("yeah ! your answer is: ", result)


divide(13, 2)
divide(3, 0)

try:
    x>3
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The try except block is finished")
