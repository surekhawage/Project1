price = float(input("Enter the cost of your bike to see your tax to be paid\n"))

if price > 100000:
    print("The tax to be paid is: RS.", price*15/100)
elif price > 50000 <100000:
    print("The tax to be paid is: RS.", price*10/100)
elif price <=50000:
    print("The tax to be paid is: Rs.", price*5/100)
