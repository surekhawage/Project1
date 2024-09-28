print("Enter any three numbers to check the largest one\n")
number1 = int(input("number 1 :"))
number2 = int(input("number 2 :"))
number3 = int(input("number 3 :"))

if number1 > number2 > number3:
    print(f"The number {number1} is the largest number out of three ")
elif number2 >number1 >number3 :
    print(f"The number {number2} is the largest number out of three ")
elif number3 >number2 >number1:
    print(f"The number {number3} is the largest number out of three ")
elif number1 > number3 > number2:
    print(f"The number {number1} is the largest number out of three ")
elif number2 > number3 > number1 :
    print(f"The number {number2} is the largest number out of three ")
elif number3 > number1 > number2 :
    print(f"The number {number3} is the largest number out of three ")
else : 
    print("Please enter valid number")

                       #(OR)

if number1 > number2 and number1 > number3:
    print("The largest number is :", number1)
elif number2 > number1 and number2 > number3:
    print("The largest number is :", number2)
elif number3 > number1 and number3 > number2:
    print("The largest number is :", number3)
else:
    print("Please enter valid number")
