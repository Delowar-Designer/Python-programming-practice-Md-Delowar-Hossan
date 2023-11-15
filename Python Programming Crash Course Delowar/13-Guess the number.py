#--- Guess the number game in python---
import random
mynum = random.randint(1,9) #computer guess number
print("I Have a Number in My Mind, Can You Guess it? \nEnter the numbers between 1 and 9")
while True:
    userNum = int(input("nter Your Guess: "))

    if userNum == mynum:
        print("Yes You are Right")
        break
    elif userNum > mynum:
        print("My Number is greater than the number you entered \nEnter the numbers between 1 and 9 \nSorry Try Agin!")
    else:
        print("My Number is less than the number you entered \nEnter the numbers between 1 and 9 \nSorry Try Agin!")