#------------------------------------------------------------------------------
#           Importing Classes
#------------------------------------------------------------------------------
from first_module import Robot as r
from first_module import Human as h


robot = r("Mitu", "19 years")
human = h("Joty","22 years","Marite")

robot.show_name()
robot.show_age()

human.show_name()
human.show_age()
human.show_food()



import first_module as f

robot = f.Robot("Mitu", "19 years")
human = f.Human("Joty","22 years","Marite")

robot.show_name()
robot.show_age()

human.show_name()
human.show_age()
human.show_food()

from second_module import Animal as a

animal = a("Majdur","20 years","Narse","pet Animal")

animal.show_name()
animal.show_age()
animal.show_food()