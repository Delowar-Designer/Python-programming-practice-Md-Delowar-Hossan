#------------------------------------------------------------------------------
#           Encapsulation
#------------------------------------------------------------------------------
class Nobita:
    def __init__(self):
        self.book = "Comics"
        self.no = 30
        self._no = 20
        self.__no = 40
        
        
    def show(self):
        print(self.no,self._no,self.__no)
        
    def change_book_count(self):
        self.__no =100
        

class Sonio(Nobita):
    def show_nobita(self):
        print("Sonio:",self._Nobita__no)
        

class Shizuka(Nobita):
    def show_nobita(self):
        print("Shizuka:",self.no)



nobita = Nobita()
sonio = Sonio()
shizuka = Shizuka()

print(sonio._Nobita__no)

nobita.show()
#nobita.__no = 100
nobita.change_book_count()

nobita.show()
sonio.show_nobita()
shizuka.show_nobita()



