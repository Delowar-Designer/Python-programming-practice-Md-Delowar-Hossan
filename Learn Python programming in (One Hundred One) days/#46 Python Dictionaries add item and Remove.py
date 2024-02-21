#46 Python Dictionaries add item and Remove
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
# StudentInfo.pop("Delowar")
# StudentInfo.pop("Year")

StudentInfo.popitem()
StudentInfo.popitem()
StudentInfo.popitem()
print(StudentInfo)