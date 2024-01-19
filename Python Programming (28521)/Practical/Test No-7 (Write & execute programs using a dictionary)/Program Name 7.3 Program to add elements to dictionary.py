# Program to add elements to dictionary
my_cars = {}  # create an empty dict
print("My empty Dict: ",my_cars)

my_cars.setdefault('Cars',[]).append("BMW") # add a car
print("First ltem Added: ",my_cars)

my_cars.setdefault('Cars',[]).append("Toyota Delowar") # add a second car
print("Second ltem Added: ",my_cars)

my_cars.setdefault('Cars',[]).append("Honda") # add a third car
print("Third ltem Added: ",my_cars)

