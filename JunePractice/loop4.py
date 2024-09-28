number = int(input("Enter any number to see their factorial\n"))
fact= 1

for i in range(1,number+1):
    fact *=i
    
print(f"The factorial of number :{number} is:",fact)
