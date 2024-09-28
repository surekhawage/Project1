number  = int(input("Enter a number to check whether the last digit of that number is divisible by 3 or not\n"))

mod = number % 10

if mod%3 == 0:
    print("The last digit of the number entered is divisible by 3")
else:
    print("The last digit of the number entered is not divisible by 3")

