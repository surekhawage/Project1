class Value:
    def __init__(self):
        self.type= "portable"
        self.model= "AT"
        self.number= 20

    def all_values(self):
        return f"{self.type},{self.model},{self.number}"
    
v1= Value()
print(v1.all_values())
