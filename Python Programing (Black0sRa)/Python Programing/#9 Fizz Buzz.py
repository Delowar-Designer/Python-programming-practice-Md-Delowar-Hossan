# Fizz Buzz
number = 15
if number % 3 == 0 and number % 5 == 0:
    if number % 5 == 0:
        print("FizzBuzz1")
    print(number, "FizzBuzz")
elif number % 5 == 0:
    print(number,"Buzz")
elif number % 3 == 0:
    print(number,"Fizz")

print("Finished")