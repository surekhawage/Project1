class Student:
    def __init__(self):
        print('non parameterized constructor - student created')
    def __del__(self):
        print('Destrutor called, student deleted.')

s1= Student()
s2= Student()
del s1

 