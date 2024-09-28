class Area:
    def p(self,x,y=None):
        if y is not None:
            print("Area of Rectangle:", x*y)
        else:
            print("Area of Square=", x*x);
a = Area()
a.p(10)
a.p(10,20)

