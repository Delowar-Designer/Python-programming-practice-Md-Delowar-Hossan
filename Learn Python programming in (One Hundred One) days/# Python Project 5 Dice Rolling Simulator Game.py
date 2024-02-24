# Python Project 5 Dice Rolling Simulator Game
import random

DiceRolling = True
while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input("Do You Want To Roll Again [y/n]:")
    if PlayAgain == "y":
        continue
    else:
        print("Game over")
        break