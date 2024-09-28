class Animal:
    def makesound(self):
        pass
class Dog(Animal):
    def makesound(self):
        print("Woof!")

class Cat(Animal):
    def makesound(self):
        print("Meow!")

d1= Dog()
c1= Cat()

d1.makesound()
c1.makesound()
