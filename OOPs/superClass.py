class Parent(object):
    def __init__(self,mssg):
        print(mssg,'Parent class')

class Child(Parent):
    def __init__(self):
        super().__init__('Hello')

a1 = Child()
