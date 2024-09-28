# Q8. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
# Unit
# Price
# First 100 units
# no charge
# Next 100 units
# Rs 5 per unit
# Rs 10 per unit
# After 200 units
# (For example if input unit is 350 than total bill amount is Rs2000)


units = int(input("Enter number units of electricity bill to see the bill Amount\n"))

if units <=100 :
    # price1 = units*10
    print("You have no bill charges to pay because the units are less than 100")

elif units >= 101 > 200:
    # price1 = 100*10
    price2 = 5*(units - 100)
    final_price = price2

    print("The bill amount is :", final_price)

elif units >200:
    # price1 = 100*10
    price2 = 100*5
    price3 = 10*(units - 200)
    final_price2 = price2 + price3

    print("The bill amount is :", final_price2)

else :
    print("Please enter valid unit number")

