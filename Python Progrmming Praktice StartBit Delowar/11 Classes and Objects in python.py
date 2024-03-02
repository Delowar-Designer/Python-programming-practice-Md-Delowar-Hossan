# Classes and Objects
class User:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email = input("Enter email: ")
        password = input("Enter Password: ")
        if email == self.email and password == self.password:
            login = True
            print("Login Successfful!")
        else:
            print("Login Faild!")

    def logout(self):
        login = False
        print("logged out!")

    def isloggedin(self):
        if self.login:
            return True
        else:
            return False
    def profle(self):
        if self.isloggedin():
            print(self.name,"\n",self.email)
        else:
            print("User is not Logged in!")

user1 = User()
user1.name = "Delowar"
user1.email = "delowar@gmail.com"
user1.password = "123456"

user1.login()
user1.profle()

hello = input()

