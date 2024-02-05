# Use the Del ky-oward method to remove the item with the specified key name
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print("Before using del keyword:")
print(thisdict)
del thisdict
print("After using del keyword:")
print(thisdict) # this will cause an error because "thisdict" no longer ecist
