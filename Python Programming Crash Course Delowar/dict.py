employee = {
    "firs_name":"john",
    "last_name":"Doe",
    "age": 24,
    "salary": 25000,
    "company":"GooGLE"
}
print(employee)
#acces first name
print(employee["firs_name"])
x = employee["salary"]
print("The salary is : ",x)
#add items
employee["coach"] = "Delowar"
print(employee)
#change the value of existing item
employee["company"] = "DD"
print(employee)
#removing on item
employee.pop("age")
print(employee)
#removig ant item using del keyword
del employee["firs_name"]
print(employee)

#create dictionary using dict() method
bangladesh_team = dict(
    {
        "captain":"virat",
        "viceCaptain":"rohit"
    }
)
print(bangladesh_team)

#nested Dictionary
delowar_team = {
    "manager": {
        "name":"ravi shastrt"
    },
    "player": {
        "captain": "virat",
        "engore": "2"
    },
    "allRounder": {
        "fall": "pandya",
        "sall": "jadeja"
    }
}
print("The is Nested Dictionary :",delowar_team)
print(
    delowar_team["player"]["engore"]
)