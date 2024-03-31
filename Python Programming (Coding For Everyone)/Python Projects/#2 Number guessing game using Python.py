#2 Number guessing game using Python
import random
import math
lower = int(input("please enter lower limit: "))
upper = int(input("please enter upper limit: "))

guess = int(input("please guess the number: "))

if guess<lower or guess>upper:
    print("plese enter your number between the range: ")
else:
    random_number = random.randint(lower, upper)
    chance = round(math.log(upper-lower+1,2))

    while chance>0:
        chance = chance - 1
        if guess>random_number:
            print("too high")
        elif guess<random_number:
            print("too low")
        else:
            print("You guessed it right, the number was", random_number)
            break
        if chance!=0:
            print("you have only",chance, "chances left")
            guess = int(input("please guess the number: "))
        else:
            print("you have exhausted all your chances")
