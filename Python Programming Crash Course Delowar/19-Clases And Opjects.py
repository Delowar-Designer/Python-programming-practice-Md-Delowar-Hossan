#----- Advance python ----

# Clases create
class person:
    # body of person class
    # class properties
    first_name = "Delowar"
    ladt_name = "Hossan"
    age = 19
person_obj = person() # cladd object
#access properties
firstName = person_obj.first_name
ladtName = person_obj.ladt_name
Age = person_obj.age
# print the values of person class
print("First Name: ",firstName)
print("Last Name: ",ladtName)
print("Age: ",Age)


# class with attribute
# creating on instance of the class
class student:
    def __init__(self,id_number,name,age):
        self.id_number =id_number
        self.name =name
        self.age =age
    def greet_student(self):
        print("Hello " + self.name + ", How are You?")


student1 = student(1414,"Mitu",22) # instance
student2 = student(1515,"Joty",25)



x = student1.id_number
y = student1.name
z = student1.age

student1.greet_student()
print("Student one Roll no is:",x)
print("student one Name is:",y)
print("Student one Age is:",z)
#instance are always unique
student2.greet_student()
print("Student 2 id is:",student2.id_number)
print("Student 2 Name is:",student2.name)
print("Student 2 age is:",student2.age)
