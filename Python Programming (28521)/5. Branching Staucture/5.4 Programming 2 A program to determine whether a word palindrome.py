# A program to determine whether a word palindrome is a word, number,
# or sequence that, when reversed, has the same thing as 707 or Madam not.
word = input("input your word: ")
word = word.casefold()
reversed_word= word[::-1]
if word == reversed_word:
    print(word,"is pallindrome ")
if word not in reversed_word:
    print(word,"is not a Pallindrome ")
