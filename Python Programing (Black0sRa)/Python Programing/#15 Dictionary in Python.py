# Dictionary in Python
dictionary = {
    "Name" : "Mitu",
    "Age" : 21,
    "Gender" : "Female",
    "Phone Number" : "+44 123 456"
}
print(dictionary)
print(dictionary["Name"])
print(dictionary.get("Phone Number"))
print(dictionary.get("weight", "You entered an Invalid Value"))
