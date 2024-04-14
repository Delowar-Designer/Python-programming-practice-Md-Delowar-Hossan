# Encapsulation with Example
class Fish:
    def __init__(self):
        self.__size = "big"
    def get_size(self):
        print("I am " + self.__size + " fish")
    def set_size(self, new_size):
        self.__size = new_size
# using the getter method
oscar = Fish()
oscar.get_size() # => I am big fish
# change the size
bert = Fish()
bert.__size = "small"
bert.get_size() # => I am big fish
# using setter method
fin = Fish()
fin.set_size("tiny")
fin.get_size() #=> I am a tiny fish