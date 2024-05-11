# Guessing game in python
import random

secret = random.randint(1,100)
i = 1
while(i <= 3):
    guess = int(input('Guess The number: '))
    if(secret == guess):
        print('Correct Guess')
        break
    else:
        print('wrong Guess.')
        i+=1
