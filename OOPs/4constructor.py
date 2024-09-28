class Student:
    count = 0;
    def __init__(self):
        Student.count= Student.count+1

s1= Student()
s2= Student()
print("The number of objects are :", Student.count)
