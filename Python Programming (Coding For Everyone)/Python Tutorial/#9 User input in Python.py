#9 User input in Python
'''name = int(input("Enter your number: "))
nume1 = int(input("Enter your first number: "))
print(name+nume1)
'''
'''num2 = eval(input("Please enter en expression"))
print(num2)'''
'''ch = input("Do you want to ")[0]
print(ch)'''

import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(num1+num2)