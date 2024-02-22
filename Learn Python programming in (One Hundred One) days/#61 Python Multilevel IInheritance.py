#61 Python Multilevel IInheritance
class baba():
    car = "BME"
    tk = "100 Crore"
    Home = "10 Floor"

class son1(baba):
    SmartPhone = "Iphone"
    Ac = "Walton"
    Microphone = "Fifine"

class son2(son1):
    Webcam = "Iphone"
    Laptob = "Ealton"
    Camera = "Fifine"

class sun3(son2):
    BrokernPhone = ""
    BrokenHome = ""

k = sun3()
print(k.Microphone)
