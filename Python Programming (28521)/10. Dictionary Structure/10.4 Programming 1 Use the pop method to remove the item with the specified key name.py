# Use the pop method to remove the item with the specified key name
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print("Befor Removing item: ")
print(thisdict)
print("After Removing item: ")
thisdict.pop("model")
print(thisdict)