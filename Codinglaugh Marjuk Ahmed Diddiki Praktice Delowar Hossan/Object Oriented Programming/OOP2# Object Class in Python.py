#------------------------------------------------------------------------------
#               Object Class in Python
#------------------------------------------------------------------------------
class ProgramerDelowar:
    pass

ob1 = ProgramerDelowar()

ob1.name = "Delowar"
ob1.age = 1

print(ob1.name)
print(ob1.age)


class Cartoon:
    series = "Tv series"
    
ob1 = Cartoon()
ob2 = Cartoon()

ob2.name = "Doreamon"
ob2.age = 5

ob1.name = "Shinchan"
ob1.age = 5

print(ob2.name)
print(ob2.age)
print(ob2.series)
print()
print(ob1.name)
print(ob1.age)
print(ob1.series)

#------------------------------------------------------------------------------
#     init Class
#------------------------------------------------------------------------------
class Cartoon:
    series = "Tv series"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
ob1 = Cartoon("Doraemon",20)
ob2 = Cartoon("Shinchan",5)

print(ob2.name)
print(ob2.age)
print(ob2.series)
print()
print(ob1.name)
print(ob1.age)
print(ob1.series)


#------------------------------------------------------------------------------
#          Class Method
#------------------------------------------------------------------------------
class Cartoon:
    series = "Tv series"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
        
ob1 = Cartoon("Doraemon",20)
ob2 = Cartoon("Shinchan",5)
ob3 = Cartoon("Mitu",45)

ob1.show()
ob2.show()
ob3.show()

#------------------------------------------------------------------------------
#          Modify object Properties
#------------------------------------------------------------------------------
class Cartoon:
    series = "Tv series"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
        
ob1 = Cartoon("Doraemon",20)
ob2 = Cartoon("Shinchan",5)
ob3 = Cartoon("Mitu",45)

ob3.age = 19

ob1.show()
ob2.show()
ob3.show()

#------------------------------------------------------------------------------
#          Delete object Properties
#------------------------------------------------------------------------------
class Cartoon:
    series = "Tv series"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
        
ob1 = Cartoon("Doraemon",20)
ob2 = Cartoon("Shinchan",5)
ob3 = Cartoon("Mitu",45)

del ob1.age

#ob1.show()
ob2.show()
ob3.show()

#------------------------------------------------------------------------------
#          Delete object
#------------------------------------------------------------------------------
class Cartoon:
    series = "Tv series"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
        
ob1 = Cartoon("Doraemon",20)
ob2 = Cartoon("Shinchan",5)
ob3 = Cartoon("Mitu",45)


del ob1

ob1.show()
ob2.show()
ob3.show()


#------------------------------------------------------------------------------
#          Built in Methods in _doc_
#------------------------------------------------------------------------------
class Cartoon:
    "This is a Cartoon class"
    series = "Tv series" #class Variable
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
    
print(Cartoon.__doc__)



#------------------------------------------------------------------------------
#          Built in Methods in __dict__
#------------------------------------------------------------------------------
class Cartoon:
    "This is a Cartoon class"
    series = "Tv series" #class Variable
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
    

ob1 = Cartoon("Doraemon",20)
ob2 = Cartoon("Shinchan",5)
ob3 = Cartoon("Mitu",45)

print(ob1.__dict__)