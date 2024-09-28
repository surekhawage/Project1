from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def description(self):
        print("This is a shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.14*self.radius**2
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length= length
        self.width= width
    
    def area(self):
        return self.length*self.width

c1= Circle(3)
r1= Rectangle(2,4)

print(c1.area())
print(r1.area())
c1.description()
r1.description()
