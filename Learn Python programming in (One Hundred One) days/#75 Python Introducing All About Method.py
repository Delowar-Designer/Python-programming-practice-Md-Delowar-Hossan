#75 Python Introducing All About Method
class parentInfo:
    def __init__(self,Name, Number):
        print(f"My Name is {Name}, & My Numbers is {Number}")

    def YourName(self,Number):
        self.Number = Number

        print(Number)

    @classmethod
    def MyName(LMS):
        print("hello Python")

p2 = parentInfo("Delowar","0177387009038")
parentInfo.MyName()
p2.YourName("Delowar")


class ClassName:
    def InstanceMethod(selfself):
        print("Hello Instance Method")

    @classmethod
    def ClassMethod(cls):
        print("This is class Method")

    @staticmethod
    def StaticMethod():
        print("Thiis is StaticMethod")

v1 = ClassName()
v1.InstanceMethod()
v1.ClassMethod()
ClassName.ClassMethod()
v1.StaticMethod()
