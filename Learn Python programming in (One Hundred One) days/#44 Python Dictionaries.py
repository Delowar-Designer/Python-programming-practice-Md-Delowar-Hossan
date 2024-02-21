#44 Python Dictionaries
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
print(StudentInfo["Year"])

x = StudentInfo.get("Delowar")
print(x)

y = StudentInfo.keys()
print(y)

print(StudentInfo.values())
