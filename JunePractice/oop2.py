class Calculator:
    def __init__(self,num1,num2):
        self.num1= num1
        self.num2= num2

    def add(self):
        add_result = self.num1 + self.num2
        return add_result
    
    def sub(self):
        sub_result = self.num1 - self.num2
        return sub_result
    
    def multiplication(self):
        mul_result = self.num1 * self.num2
        return mul_result
    
    def division(self):
        if self.num2 == 0:
            print("Divsion error :Division by zero is not allowed")
        else :
            return self.num1/num2
    
    def square(self):
        return self.num1*self.num1, self.num2*self.num2




print("For Basic Arithematic operations like :\nAddition, Substraction, Division, Multiplication, Square of both numbers \nEnter two numbers\n")
num1= int(input("Number 1 = "))
num2= int(input("Number 2 = "))
    
c1= Calculator(num1,num2)

print("Addition is :", c1.add())
print("Subtraction is :", c1.sub())
print("Multiplication is :", c1.multiplication())
print("Division is :", c1.division())
print("Sqaure of both number respectively is :", c1.square())


while True:
    print("\nWant to enter numbers Again? type y/n:")
    response = input()
    if response =="y":
        num1= int(input("\nNumber 1 = "))

        if num1 ==int:
            continue
        else:
            print("Enter integer numbers only")

        num2= int(input("Number 2 = "))
        
        if num2 ==int:
            continue
        else:
            print("Enter integer numbers only")
 
        c1= Calculator(num1,num2)

        print("Addition is :", c1.add())
        print("Subtraction is :", c1.sub()) 
        print("Multiplication is :", c1.multiplication())
        print("Division is :", c1.division())
        print("Sqaure of both number respectively is :", c1.square())
    elif response =="n":
        break

    else:
        print("Invalid input. please type y/n :")

c1.add()
c1.sub()
c1.multiplication()
c1.division()
c1.square()