num1= int(input("Enter number to check whether it is a palindrome or not"))

dig= num1
rev= 0
num2= 0

while dig>0:
    rev = rev*10+ dig%10
    dig = int(dig/10)

if(rev==num1):
    print("The entered number is palindrome")
else:
    print("The entered number is not palindrome")    
