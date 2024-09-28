while True:
    try :
        x = int(input("enter x value ="))
        y = int(input("enter y value ="))
        print(x/y)
    except ZeroDivisionError:
        print("can't divide by zero")
    except ValueError:
        print("enter integer number only")

    while True:
        response = input("Want to enter again type y/n").lower()

        if response in ('y','n'):
            break
        
        else:
            print("Enter y/n only")

    if response =="n":
        break
