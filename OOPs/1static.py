class Maths:
    def add(x,y):
        return x+y
    
Maths.add = staticmethod(Maths.add)
print("The sum is :", Maths.add(10,20))


class Program:
    @staticmethod
    def run():
        print("Execute Program")
Program.run()

class Program:
    @staticmethod
    def run():
        print("Execute Program")
    def stop(self):
        print("Stop program")

Program.run()
s1= Program()
s1.stop()
