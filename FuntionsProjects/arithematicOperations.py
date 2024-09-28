
x= int(input("Enter first number to perform addition, substraction, multiplication, division of that number\n"))
y= int(input("Enter second number\n"))

def calculation(x,y):

    addition = x+y
    substraction = x-y
    multiplication = x*y
    division = x/y

    print("The addition of ", x,"and",y, "is :", addition)
    print("The substraction of ", x,"and",y, "is :", substraction)
    print("The multiplication of ", x,"and",y, "is :", multiplication)
    print("The division of ", x,"and",y, "is :", division)

    return

calculation(x,y)