# Exception Handling (part-2)
'''try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 / num2
    print(result)

except (ValueError,ZeroDivisionError):
    print("You have to entered incorrect input.")

#except ZeroDivisionError:
    #print("You can not Divide a number by 0")

finally:
    print("Goodbye ! ! !")
'''


def voter (age):
    if age < 18:
        raise ValueError("Invalid Voter Age")
    return "You are allowed to vote"

try:
    print(voter(17))
except ValueError as e:
    print(e)
