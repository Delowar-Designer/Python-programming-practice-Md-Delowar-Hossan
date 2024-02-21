#47.2 Python Copy Dictionary
student = {
    "sum1" : 20,
    "sum2" : 40,
    "sum3" : 60
}

print(student)
myDict = student.copy()
print(myDict)

x = dict(student)
print(x)