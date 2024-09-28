number = int(input("Enter any number to see its reverse\n"))

# using for loop

numbers = str(number)

x = ""
for i in reversed(numbers):
    x += i

y = int(x)


print("reverse is",y )

# using While loop 

# sign = -1 if number <0 else 1
# y1 =0

# n = abs(number)

# while n != 0 :
#     x1 = n%10
#     y1 = y1*10 +x1
#     n //=10

# reverse = y1*sign
# print(reverse)

# using reversed function
# numbers = str(number)

# reverse = reversed(numbers)
# a1= "".join(reverse)
# print(a1)

