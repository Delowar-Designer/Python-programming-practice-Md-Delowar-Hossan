# Boc object
class Box:
    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.depth = d
    def box_volume(self):
        return self.width*self.height*self.depth

my_box1 = Box(10, 10, 10)
my_box2 = Box(20, 20, 20)
my_box3 = Box(30, 30, 30)

print("The volume of box1 is:", my_box1.box_volume())
print("The volume of box2 is:", my_box2.box_volume())
print("The volume of box3 is:", my_box3.box_volume())



