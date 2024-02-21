#45 Python Dictionaries change item
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
StudentInfo["Year"] = 2005
print(StudentInfo)
print(StudentInfo["Year"])

StudentInfo.update({"Delowar":"Joty is an cse student"})
print(StudentInfo["Delowar"])
