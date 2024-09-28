class Rectangle:
    def __init__(self,length,width):
        self.length= length
        self.width= width

    def get_area(self):
        area_of_rectangle = self.length*self.width
        return area_of_rectangle
    
r1= Rectangle(6,3)
print(r1.get_area())


        