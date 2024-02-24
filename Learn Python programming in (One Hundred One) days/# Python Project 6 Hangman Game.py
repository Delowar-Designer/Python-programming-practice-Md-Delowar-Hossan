# Python Project 6 Hangman Game
word = "Delowar"
chances = 7
GuessAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end = " ")
        else:
            print(" ", end = "")

    MyGuess = input(f"Your Changes Is{chances}, Guess The Letter: ")
    GuessAdd.append(MyGuess.lower())
    if MyGuess.lower() not in word.lower():
        chances = chances - 1
        if chances == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in GuessAdd:
            done = False

if done:
    print(f"yes, you have won the game, the word is {word} ")
else:
    print("you loss the game")

