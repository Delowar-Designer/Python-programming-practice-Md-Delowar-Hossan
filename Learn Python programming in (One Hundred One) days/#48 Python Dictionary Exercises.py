#48 Python Dictionary Exercises
# use the get method to print the value of the "mode" key off the car dictionary.
car = {
    "brand": "Ford",
    "model": "Mercedes",
    "year": 2004
}
print(car)
print(car.get("model"))
car["year"] = 2005
print(car)