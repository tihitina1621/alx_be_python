class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
import math
class Circle(Shape):
    def __init__(self, radius):
        self.radius =  radius
    def area(self):
        return math.pi * self.radius** 2
shapes = [Rectangle(10, 5),
        Circle(7)]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    

