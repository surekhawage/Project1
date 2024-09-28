class Area:
    def __init__(self,radius):
        self.radius= radius

    def get_radius(self):
        area_of_circle = 3.14*self.radius*self.radius
        return area_of_circle
    
a1= Area(4)
print(a1.radius)
print(a1.get_radius())
