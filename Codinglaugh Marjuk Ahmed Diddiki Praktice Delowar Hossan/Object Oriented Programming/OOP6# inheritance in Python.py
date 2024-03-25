#------------------------------------------------------------------------------
#           inheritance
#------------------------------------------------------------------------------
class Doreamon:
    def doreamon_self(self):
        print("I am Doreamon I come from the future")
        
    def gadget(self):
        print("New Godget.",end="\n\n")
        
class Nobita(Doreamon):
    def nobita_self(self):
        print("I am Nobita. I hobby is sleep.",end="\n\n")
        
class Shizuka(Nobita):
    def shizuka_self(self):
        print("I am Shizuka. I hobby is singing.",end="\n\n")
        

doreamon = Doreamon()
nobita = Nobita()
shizuka = Shizuka()

#nobita.gadget()
shizuka.gadget()


#------------------------------------------------------------------------------
#           Hierarchical Inheritance
#------------------------------------------------------------------------------
class Doreamon:
    def doreamon_self(self):
        print("I am Doreamon I come from the future")
        
    def gadget(self):
        print("New Godget.",end="\n\n")
        
class Nobita(Doreamon):
    def nobita_self(self):
        print("I am Nobita. I hobby is sleep.",end="\n\n")
        
class Shizuka(Doreamon):
    def shizuka_self(self):
        print("I am Shizuka. I hobby is singing.",end="\n\n")
        

doreamon = Doreamon()
nobita = Nobita()
shizuka = Shizuka()

#nobita.gadget()
shizuka.gadget()


#------------------------------------------------------------------------------
#           Multiple Inheritance
#------------------------------------------------------------------------------
class Doreamon:
    def doreamon_self(self):
        print("I am Doreamon I come from the future")
        
    def gadget(self):
        print("New Godget.",end="\n\n")
        
class Nobita:
    def nobita_self(self):
        print("I am Nobita. I hobby is sleep.",end="\n\n")
        
class Shizuka(Doreamon,Nobita):
    def shizuka_self(self):
        print("I am Shizuka. I hobby is singing.",end="\n\n")
        

doreamon = Doreamon()
nobita = Nobita()
shizuka = Shizuka()

#nobita.gadget()
shizuka.nobita_self()
shizuka.doreamon_self()
