# def method_(a, b):
#     print("A method")
#
# class Person:
#     def __init__(self, person_name: str, year_of_birth: int, ht_inches: int =None):
#         self.__name = person_name
#         self.__date_of_birth = year_of_birth
#         self.__height = ht_inches
#         self.abc = None
#
#     def get_year_of_birth(self):
#         return self.__date_of_birth
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, new_name):
#         return self.__name
#
#     def set_name(self, new_name):
#         if self.__has_any_number(new_name):
#             print("Sorry person nname can't have numbdr")
#             return
#         self.__name = new_name
#     def __has_any_number(self, string):
#         return "0" in string
#
#     def get_summary(self):
#         return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self._height}"
#
#
# person_list = [Person("Delowar", 2004, 60),
#                Person("Joty", 1993, 72),
#                Person("Mitu", 1980, 30),
#                Person("Mijdur", 2020, 65),
#                Person("Yafta", 1900, 40)]
#
# for person in person_list:
#     if person.get_year_of_birth() >= 1990:
#         print(person.get_summary())

class Person:
    def __init__(self, person_name: str, year_of_birth: int, ht_inches: int = None):
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches

    def get_year_of_birth(self):
        return self.__date_of_birth

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name is None or new_name == "":
            print("Name cannot be empty.")
            return
        if self.__has_any_number(new_name):
            print("Sorry, person name can't have numbers.")
            return
        self.__name = new_name

    def __has_any_number(self, string):
        return any(char.isdigit() for char in string)

    def get_summary(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height if self.__height is not None else 'Invalid'}"


person_list = [Person("Delowar", 2004, 60),
               Person("Joty", 1993, 72),
               Person("Mitu", 1980, 30),
               Person("Mijdur", 2020),
               Person("Yafta", 1900, 40)]

for person in person_list:
    if person.get_year_of_birth() >= 1990:
        print(person.get_summary())


class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, email_id: str, student_id: str):
        super().__init__(person_name, year_of_birth)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"

    def __str__(self):
        return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"

    def __repr__(self):
        return f"Name: {self.get_name()} Email: {str(self.email)} Birth: {self.get_year_of_birth()}"

student = Student("A", 2000, "a@google.com", "12234jhsihiu")
print(student)
student.set_name("Delowar")
print(student)


class Teacher(Person):
    def __init__(self, person_name: str, year_of_birth: int, department_id: str):
        super().__init__(person_name, year_of_birth)
        self.dept = department_id

new_person_list = [
    Person("Delowar", 2004),
    Student("Mitu", 2000, "matu@gmail.com", "stid"),
    Teacher("Joty", 1980, "Bangla")
]

for p in new_person_list:
    print(p.get_name())

