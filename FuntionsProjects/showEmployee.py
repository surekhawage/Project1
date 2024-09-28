name= str(input("Enter the name of the employee in the folowing to see there salary\nSumit\nHarish\nGaurav\nMohit\n"))

def company(name, salary= 15000):

    if(name== "sumit"):
        print("The salary of",name,"is : 20000")

    elif(name== "harish"):
        print("The salary of",name,"is : 25000")

    elif(name== "gaurav"):
        print("The salary of",name,"is : 22000")

    elif(name== "amit"):
        print("The salary of",name,"is : 30000")

    else:
        print("The salary of",name,"is :",salary)

    return

company(name)
        

