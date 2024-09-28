class Father:
    def display(self):
        print("Father")

class Mother:
    def display2(self):
        print("Mother")
class Son(Mother,Father):
    def display3(self):
        print("Son")

s1= Son()
s1.display3()
s1.display2()
s1.display()

