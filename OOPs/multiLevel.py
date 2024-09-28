class GrandFather:
    def display(self):
        print("Grandfather")

class Father(GrandFather):
    def display2(self):
        print("Father")
    
class Son(Father):
    def display3(self):
        print("Son")
    
s1= Son()
s1.display()
s1.display2()
s1.display3()
