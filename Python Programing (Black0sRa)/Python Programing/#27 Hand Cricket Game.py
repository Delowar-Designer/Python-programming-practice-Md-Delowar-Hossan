# Hand Cricket Game
import random as rd

score = 0
while True:
    player_1 = int(input("Player 1: "))
    player_2 = rd.randint(1,7)
    if player_1 >7 or player_1 < 1:
        print("Pls, entervalid value (1 - 7)")
        continue
    else:
        if player_1 != player_2:
            score += player_1
            print(f"Player 2: {player_2}")
        else:
            print(f"Player 2: {player_2}")
            print("OUT!!!!!!!")
            break
print(f"Your Score is: {score}")
