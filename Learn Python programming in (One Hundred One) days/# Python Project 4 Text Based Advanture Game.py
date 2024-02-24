# Python Project 4 Text Based Advanture Game
answer = input("Do you want to play this game? [Yes/No]: ")

if answer == "Yes":
    print("Welcome to the game!")
    answer = input("do you want to go Jungle or cave? [jungle/cave]:")
    if answer == "jungle":
        print("you see the hungry tiger. Tiger will eat you. game close")
    elif answer == "cave":
        print("you seen the bear in front of cave")
        answer = input("do you want to fight with the ber or run away! [fight/run] ")
        if answer == "fight":
            print("bear is too much strong! you loss the game!")
        else:
            print("wow! still you Are alive!")
else:
    print("The Game Closed")
