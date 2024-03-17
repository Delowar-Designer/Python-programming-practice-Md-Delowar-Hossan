#------------------------------------------------------------------------------
#           Spcial Magic Method
#------------------------------------------------------------------------------
a = 5
b = 6
print(a+b)
print(a-b)


print(a.__add__(b))
print(a.__sub__(b))



class Number:
    def __init__(self,no):
        self.no = no
        
    def __add__(self,jeita_seita):
        return self.no + jeita_seita.no +2
        #return "Delowar is a bat boy"
    
    def show(self):
        print(self.no)
        
a = Number(7)
b = Number(10)

print(a.__add__(b))
