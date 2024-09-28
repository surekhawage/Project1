class Shape:

    def __init__(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius= radius

    def area(self):
        a = 3.14*self.radius*self.radius
        return a
    
    def perimeter(self):
        p = 2*3.14*self.radius
        return p
    
class Triangle(Shape):
    def __init__(self,breadth,height,a,b,c):
        self.breadth= breadth
        self.height = height
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        a = 0.5*self.breadth*self.height
        return a
    
    def perimeter(self):
        p = self.a + self.b + self.c
        return p
    
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        a = self.side*self.side
        return a
    
    def perimeter(self):
        p = self.side*4
        return p
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length= length
        self.breadth = breadth

    def area(self):
        a = self.length*self.breadth
        return a
    
    def perimeter(self):
        add = self.length + self.breadth
        b = 2*add
        return b
    
c1 = Circle(3)
t1 = Triangle(4,8,3,4,3)
s1 = Square(4)
r1 = Rectangle(8,4)

print(f"The area of Circle is :{c1.area()}","and perimeter is :",{c1.perimeter()})
print("The area of Triangle is :",{t1.area()},"and perimeter is :",{t1.perimeter()})
print("The area of Square is :",{s1.area()},"and perimeter is :",{s1.perimeter()})
print("The area of Rectangle is :",{r1.area()},"and perimeter is :",{r1.perimeter()})

c1.area()
t1.area()
s1.area()
r1.area()

c1.perimeter()
t1.perimeter()
s1.perimeter()
r1.perimeter()
