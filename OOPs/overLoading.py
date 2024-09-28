class Test:
    print("Hello"+"Mohit")

class A:
    def __init__(self,a):
        self.a = a

    def __add__(self,o):
        return self.a + o.a
    
t1= A(10)
t2= A(20)
t3 = A("Hello")
t4 = A("Python")

print(t1+t2)
print(t3+t4)

