#------------------------------------------------------------------------------
#           nested Class
#------------------------------------------------------------------------------

class Human:
    def __init__(self, name):
        self.name = name
        
    def show_info(self):
        print(self.name)
        print("Human Class")
        
    class Robot:
        def __init__(self, name):
            self.name = name
           
        def show_name(self):
            print(self.name)
            print("Robot Class")
            
        class Robo:
            def __init__(self, name):
                self.name = name
               
            def show_details(self):
                print(self.name)
                print("Robo Class")
                




#robot = Robot("Mitu")
human = Human("Mitu")
robot = Human.Robot("Sophiya")
robo = human.Robot.Robo("Joty")

robo.show_details()

robot.show_name()
human.show_info()

#human.show_info()
#human.show_name()

