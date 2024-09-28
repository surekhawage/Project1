number = int(input("Enter any number to check whether it is a prime number or not\n"))

if number > 1:
    for i in range(2,number):
       if number%i ==0 :
            print(f"The {number} is not prime number")
            break
    else :
        print(f"The {number} is prime number")
else :
    print(f"The {number} is not prime number")

