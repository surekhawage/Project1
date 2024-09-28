
print("Enter three numbers to see who is second largest number out of three")
number1  = int(input("number 1:"))
number2  = int(input("number 2:"))
number3  = int(input("number 3:"))

if (number1 > number2 and number1 < number3) or (number1 < number2 and number1 > number3) :
    print(f"The second largest number is:", number1)
elif (number2 > number1 and number2 < number3) or (number2 < number1 and number2 > number3):
    print(f"The second largest number is:", number2)
else :
    print("The second largest number is:", number3)





