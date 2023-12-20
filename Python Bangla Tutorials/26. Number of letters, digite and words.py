# Number of letters, digite and words
numberofWords = 0
numberofLetters = 0
numberofDigits = 0

text = input("Enter a text of numbers : ") # My Name Is Delowar Hossan age 19

for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberofLetters = numberofLetters + 1

    elif x >= '0' and x <= '9':
        numberofDigits = numberofDigits + 1

    elif x == ' ':
        numberofWords = numberofWords + 1

print("Number of Letters : ",numberofLetters)
print("Number of Digits : ",numberofDigits)
print("Number of Word : ",numberofWords)


