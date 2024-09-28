class Student:
    def __init__(self,name,sex,course,result):
        self.name = name
        self.sex= sex
        self.course = course
        self.result = result

    def display(self):
        # self.name = name
        # self.sex= sex
        # self.course = course
        # self.result = result
        print('Name:', self.name)
        print('Sex:', self.sex)
        print('course:', self.course)
        print('result:', self.result)

s1= Student('vijay patil','Male','MCA','91.23%')
s1.display()
