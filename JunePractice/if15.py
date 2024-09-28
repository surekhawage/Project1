number = int(input("Enter any number to check whether it is divisible by 2 or 3 or both\n"))

two = number%2
three = number%3

if two == 0 and three == 0:
    print(f"Both 2 and 3 are divisible by {number}")
elif two == 0:
    print(f"Only 2 is divisible by {number}")
elif three == 0:
    print(f"Only 3 is divisible by {number}")
else :
    print(f"{number} is not divisible by 2 or 3")
