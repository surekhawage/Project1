class Degree:
    def getDegree(self):
        print("I got a diploma degree")
class Undergraduate(Degree):
    def getDegree(self):
        print("I got a undergraduate degree")
class Postgraduate(Degree):
    def getDegree(self):
        print("I got a postgraduate degree")

d= Degree()
u= Undergraduate()
p= Postgraduate()
d.getDegree()
u.getDegree()
p.getDegree()

