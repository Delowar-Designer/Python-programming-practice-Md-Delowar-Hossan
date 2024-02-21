#60 Python Multiple Inheritance
class baba():
    car = "BME"
    tk = "100 Crore"
    Home = "10 Floor"

class baba2:
    SmartPhone = "Iphone"
    Ac = "Walton"
    Microphone = "Fifine"

class baba3:
    Webcam = "Iphone"
    Laptob = "Ealton"
    Camera = "Fifine"

class kaka(baba,baba2,baba3):
    BrokernPhone = ""
    BrokenHome = ""

k = kaka()
print(k.Webcam)
