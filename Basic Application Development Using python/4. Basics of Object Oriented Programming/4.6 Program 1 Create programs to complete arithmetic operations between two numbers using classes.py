# Create programs to complete arithmetic operations between two numbers using classes
class Calculator:
    def __init__(self, a, b):
        print("Addition:", a+b)
        print("Subtraction:", a-b)
        print("Multiplication:", a*b)
        print("Division:", a/b)
cal = Calculator(15, 5)