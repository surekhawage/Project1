
x= int(input("Enter any three number to see greatest and smallest number among them\nEnter First number :"))
y= int(input("Enter second number:"))
z= int(input("Enter third number:"))


def sum(x,y,z):

    A= max(x,y,z)
    B= min(x,y,z) 

    print("The greatest number of the three numbers", x,y,z, "is :", A)
    print("The smallest number of the three numbers", x,y,z, "is :", B)

    return 

sum(x,y,z)