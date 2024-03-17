#------------------------------------------------------------------------------
#           Abstract Class
#------------------------------------------------------------------------------
from abc import ABC, abstracctmethod

class Father(ABC):
    @abstracctmethod
    def go_school(self):
        #print("Haa, School a gechi")
        pass
    
    def result(self):
        print("Haa, School e gechi")
        
class Nobita(Father):
    def go_school(self):
        print("Haa, School e gechi")

    def playing(self):
        print("playing Football")
        
    def singing(self):
        print("singing")
    
nobita = Nobita()
nobita.go_school()
nobita.playing()