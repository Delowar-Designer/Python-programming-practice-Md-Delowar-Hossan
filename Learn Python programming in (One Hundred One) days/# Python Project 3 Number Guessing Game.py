# Python Project 3 Number Guessing Game
import random
RandomNumber = random.randrange(1,200)
#print(RandomNumber)
UserInput = int(input("Guess the number: "))

if UserInput > RandomNumber:
    print(RandomNumber)
    print("the number is to high")
elif RandomNumber > UserInput:
    print(RandomNumber)
    print("The number is too low")

else:
    print(RandomNumber)
    print("yes, you mathed the number")
