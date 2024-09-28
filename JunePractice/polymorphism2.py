class Shape:
    def calculate_Area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side= side

    def calculate_Area(self,side):
        return self.side*self.side
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def calculate_Area(self,radius):
        return 3.14*self.radius*self.radius
    
s1= Square(4)
c1= Circle(3)

print(s1.calculate_Area(s1))
print(c1.calculate_Area(c1))


