class Book:
    name="Pyhton Programming"

    def display(s1):
        print("Book name is", s1.name)

Book.display= classmethod(Book.display)
Book.display()

class Student:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    @classmethod
    def getobject(cls):
        return cls('vijay', 43)
s1= Student.getobject()
print( "Student :",s1.name,s1.age)


        
