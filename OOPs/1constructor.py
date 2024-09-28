class Rectangle(object):
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width

r = Rectangle(2,10)
print(r.area())
      