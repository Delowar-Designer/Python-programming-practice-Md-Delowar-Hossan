#---dictionary in python---
'''
dictionary_name = {
    key:value,
    key:value,
}
'''
#creating a dictionary
person = {
    "first_name":"Delowar",
    "last_name":"Hossan",
    "age":19
}
print(type(person))
print(person)

#accessing item
x = person["first_name"]    #dictinory[key]
y = person["last_name"]
z = person["age"]
print("First Name: ",x)
print("Last Name: ",y)
print("Age:",z)

# get() Method
get_method = person.get("first_name")
print(get_method)

#adding new items
person["hobby"] = "Playing Cricket"
print(person)

#chaanging an items value
person["first_name"] ="Mito"
print(person)

#removing on item value
#pop() method
person.pop("age")
print(person)

#nested dictionary
employee_data = {
    #nestted dictionary
    "manager":{
        "name":"Md Delowar",
        "age":18
    },
    "programmer":{
        "name":"Mito",
        "age":22
    },
    "salary":{
        "manager_salary":4500,
        "programer_salary":3900
    }
}
#peint manager name and age and salary
print("\nManager Data"
    "\nManager name is:",employee_data["manager"]["name"],
    "\nmanager age is:",employee_data["manager"]["age"],
    "\nmanager salary is:",employee_data["salary"]["manager_salary"],
      )
#peint programmer name and age and salary
print("\nProgrammer Data"
    "\nProgrammer name is:",employee_data["programmer"]["name"],
    "\nProgrammer age is:",employee_data["programmer"]["age"],
    "\nProgrammer salary is:",employee_data["salary"]["programer_salary"],
      )

