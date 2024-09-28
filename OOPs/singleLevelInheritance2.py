class Vehicle:
    def __init__(self,name):
        self.name= name
    def display(self):
        print("Name=", self.name)

class Category(Vehicle):
    def __init__(self,name,price):
        Vehicle.__init__(self,name)
        self.price = price
    def disp_price(self):
        print("Price$:", self.price)

car1= Category("Maruti", 2000)
car1.display()
car1.disp_price()
car2= Category("BMW", 4000)
car2.display()
car2.disp_price()
