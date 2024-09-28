class Car:
    def __init__(self,make,model,year):
        self.make= make
        self.model= model
        self.year= year

    def drive(self):
        print("The car is driving.")

c1= Car("Toyota","Inova",2020)
print(c1.make)
print(c1.model)
print(c1.year)
c1.drive()
