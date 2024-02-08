class Point:
    def __init__(self, x, name):
        self.x = x
        self.name = name

    def move(self):
        print(f'move method executed with name: {self.name}')

    def draw(self):
        print("draw method executed")


point1 = Point(10, "Nate")
#the .x below is setting an attribute to the class
print(point1.x)
point1.move()
