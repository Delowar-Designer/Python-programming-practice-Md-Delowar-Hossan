 #47 Python Loop Dictionary
StudentInfo = {
    "Delowar": {
        "First Name": "Md Delowar Hossan",
        "study": "12",
        "Subject": "Computer Science",
        "Roll" : 602826,
        "Number" : 1773873289
    },
    "Mitu": {
        "First Name": "Md Mitu Hossan",
        "study": "13",
        "Subject": "Science",
        "Roll" : 602866,
        "Number" : 13873289
    },
"Year": 2004
}
for x in StudentInfo:
    print(x)
for a in StudentInfo.values():
    print(a)




student = {
    "sum1" : 20,
    "sum2" : 40,
    "sum3" : 60
}

for b in student.values():
    print(b)

for b in student.keys():
    print(b)

for intem in student.items():
    print(intem)