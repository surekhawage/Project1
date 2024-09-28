class Employee:
    def __init__(self,name,age,salary):
        self.name= name
        self.age= age
        self.salary= salary

    def get_salary(self):
        return self.salary

e1= Employee("Mohit",22,50000)
print(e1.name)
print(e1.age)
salary = e1.get_salary()
print(salary)

        