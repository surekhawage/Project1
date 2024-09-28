term = int(input("Enter n term to see their sum of series \n n :"))
number = int(input("Of number :"))

x = int(number)


sum = 0
for i in range(0,term):
    sum += x
    x = x*10 + number

print(f"The sum of series of number {number} and term {term} is {sum}")

