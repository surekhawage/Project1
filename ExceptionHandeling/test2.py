while True:
    try: 
         age = int(input("Enter your age for election:"))
         if age<18:
                raise Exception
         else:
             print("You are eligible for election")
             break
    except Exception:
        print("This value is too small, try again")
