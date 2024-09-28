x = int(input("Enter first value:"))
y = int(input("Enter second value:"))

try:
    result= x/y
except ZeroDivisionError:
    print("Division by Zero")
else:
    print("Result is:", result)
finally:
    print("Execute finally clause")
    