number = input('Write your phone number: ')

if len(number) > 11:
    print("Your Number is too long")
elif len(number) < 11:
    print("Your Number is too short")
elif len(number) == 11:
    print("Thank you,", number)
