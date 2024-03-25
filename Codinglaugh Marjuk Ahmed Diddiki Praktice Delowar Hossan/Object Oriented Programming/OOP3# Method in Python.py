#------------------------------------------------------------------------------
#      Instance Method in Python
#------------------------------------------------------------------------------
class Human:
    def __init__(self, name):
        self.name = name
    
    def show_name(self):
        print(self.name)
        
    def info(hey):
        print(hey.name)

        
human = Human("Mitu")

human.show_name()
human.info()

#------------------------------------------------------------------------------
#      Class Method in Python
#------------------------------------------------------------------------------
class Human:
    def __init__(self, name):
        self.name = name
    
    def show_name(self):
        print(self.name)
        
    @classmethod
    def cls_method(cls):
        print("This is a class method")
    
    @staticmethod
    def emnitei():
        print("emnitei prrint kirlam")
        
human = Human("Mitu")

human.cls_method()
Human.cls_method()
