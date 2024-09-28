number = int(input("Enter any to display its last digit\n"))

last_digit = 0

if number != 0 :
    last_digit = number % 10
    print("The last digit entered is:", last_digit)
else :
    print("Enter valid number")
