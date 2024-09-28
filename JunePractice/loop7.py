# Write a Python program to print all the Fibonacci numbers from 1 to 100 using a for loop
a = 0
b = 1

print(a)

for i in range(1,101):

    print(b)

    a,b=b,a+b
    
    if b>100:
        break
