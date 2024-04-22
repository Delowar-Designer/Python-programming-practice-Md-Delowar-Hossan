import random as rd

score = 0
while True:
    try:
        player_1 = int(input("Player 1: "))
    except ValueError:
        print("Please enter a valid integer between 1 and 7.")
        continue

    if player_1 < 1 or player_1 > 7:
        print("Please enter a valid value between 1 and 7.")
        continue

    computer = rd.randint(1, 7)
    if player_1 != computer:
        score += player_1
        print(f"Computer: {computer}")
    else:
        print(f"Computer: {computer}")
        print("OUT!!!!!!!")
        break

print(f"Your Score is: {score}")
