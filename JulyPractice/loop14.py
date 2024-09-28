

while True :

    number = int(input("Enter any number to check the total number of digits\n"))
    numbers = str(number)
    digits = len(numbers)

    print(f"The total number of digits in {number} are {digits} ")

    response = str(input("Want to enter number again type y/n\n")).strip().lower()

    if response == "n":
        break
    elif response != "y":
        print("Please enter y/n only")


