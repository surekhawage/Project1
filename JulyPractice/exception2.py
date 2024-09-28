try :
    x = int(input("enter x value ="))
    y = int(input("enter y value ="))
    print(x/y)
except (ZeroDivisionError,ValueError) as mssg:
    print("Please provide valid number is and problem is ", mssg)

