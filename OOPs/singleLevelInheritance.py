class Vehicle:
    name="Maruti";
    def display(self):
        print("Name=", self.name)

class Category(Vehicle):
    price='2000'
    def disp_price(self):
        print("price=$", self.price)
    
car1= Category()
car1.display()
car1.disp_price()
