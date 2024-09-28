class MyClass():
    pass
def value():
    return 10
a1 = MyClass()
a1.attribute1 = "Hello world"
print(a1.attribute1)

a2=MyClass()
a2.attribute2=value
value.attribute2= "Python"
print(value.attribute2)
print(a2.attribute2()==value())

