class Car:
    def get(self,color,style):
        self.color = color
        self.style = style
        
    def put(self):
        print(self.color);
        print(self.style);


c1 = Car()
c1.get("black","sedan")
c1.put()
# c1 = Car()

c1.y=2;
print(c1.y);
c1.y=3;
print(c1.y);
c1.y="Mohit";
print(c1.y);
c1.y=4.5;
print(c1.y);
c1.y= 2*2,2+1,4/2,2-3;
print(c1.y);


