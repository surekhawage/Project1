number = int(input("Enter any number to display its Multiplication table\n"))

x = 1

for i in range(1,11):
    value = number*x
    print(f"{number}x{x}={value}")
    x +=1

