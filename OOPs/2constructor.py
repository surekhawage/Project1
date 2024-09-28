class Circle():
    def __init__(self,radius):
        self.radius= radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getcircumference(self):
        return 2*3.14*self.radius
        
r = Circle(5)
print("The Area of circle:", r.getArea())
print("The circumference of circle:", r.getcircumference())
