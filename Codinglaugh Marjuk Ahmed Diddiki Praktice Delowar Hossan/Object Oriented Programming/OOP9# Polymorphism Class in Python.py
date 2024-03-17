#------------------------------------------------------------------------------
#           Polymorphism Class
#------------------------------------------------------------------------------
class Robot:
    def __init__(self, name):
        self.name = name
       
    def show_name(self):
        print(self.name)
        print("Robot Class")
        
class Human(Robot):
    def __init__(self, name):
        self.name = name
        
    def show_name(self):
        print(self.name)
        print("Human Class")
        
        
human = Human("Mitu")
robot = Robot("Joty")

human.show_name()
robot.show_name()


for i in (human, robot):
    i.show_name()


a = "Mitu"
b = " Joty"

a.__add__(b)




class Profile:
    def name(self,first=None,middle=None, last=None):
        if first!=None and middle!=None and last!=None:
            print(first+" "+middle+" "+last)
        elif first!=None and middle!=None:
            print(first+" "+middle)
        else:
            print(first)
            
p = Profile()

p.name("Md", "Delowar", "Hossan")
p.name("Mst", "Mitu", "Simai")