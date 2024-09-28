from datetime import date

class person:
    def __init__(self,name,country,DOB):
        self.name= name
        self.country= country
        self.DOB= DOB

    def calculate_age(self):
        today = date.today()
        age= today.year - self.DOB.year
        if today < date(today.year,self.DOB.month, self.DOB.day):
            age -=1
            return age
        
p1= person("Mohit","India",date(2001,12,3))

print("Name :",p1.name)
print("Country  :",p1.country)
print("DOB :",p1.DOB)
print("Age :", p1.calculate_age())


