# Use the popitem method to remove the item with the specified key name
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print("Befor using popitem()method: ")
print(thisdict)
thisdict.popitem()
print("After using popitem()method: ")
print(thisdict)