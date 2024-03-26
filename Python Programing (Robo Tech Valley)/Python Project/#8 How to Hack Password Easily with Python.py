# How to Hack Password Easily with Python
from random import *

user_x = input("Enter your x = ")

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
     's','t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
     'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1',
     '2', '3', '4','5', '6', '7', '8', '9', "@", '!', '~', '`', '#', '$', '%', '^', '&', '*',
     '(', ')', '_', '-', '=', '+', ' ', '/', '.', '[', ']', '{', '}', '|', ';', ':', '"', "'",
     ',', '<', '>', '?']


guess = ""

while (guess != user_x):
    guess = ""

    for letter in range(len(user_x)):
        guess_letter = x[randint(0, 93)]
        guess = str(guess_letter) + str(guess)
        print(guess)

print("Your x is = ", guess)