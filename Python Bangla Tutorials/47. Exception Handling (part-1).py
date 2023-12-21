# Exdeption Handling pate 1
"""num2 = int(input("Enter a number: "))
result = 20 / num2
print("The result",result)
print("Done")

text = "Delowar"
print(text[0])
print("Done")"""

try:
    list = [20,0,30]
    result = list[0] / list[3]
    print("The result",result)
    print("Done")

except ZeroDivisionError:
    print("Dividing by Zero is not Possible")

'''except IndexError:
    print("Index error")
print("successful")'''

finally:
print("Done with finally")