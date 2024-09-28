class Student:
    
    def __init__(self,name):
        print("This is a parametrized constructor")
        self.name= name
    def show(self):
        print("Hello", self.name)

s1= Student("vijay")
s1.show()
