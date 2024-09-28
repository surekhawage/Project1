class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
    
    def display(self):
        print('Employee name:',self.name)
        print('Employee age:',self.age)
        print('Employee Number:',self.eno)
        print('Employeee salary:',self.esal)

e1 = Employee('Durga',48,8181,12000)
e1.display()
e2 = Employee('Sunny',39,8182,14000)
e2.display()
