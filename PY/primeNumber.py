num= int(input("ENter any number :"))




for i in range(2,num-1):

    x=num%i
    if(x==0):
        print("it is not prime no.")
        break
    else:
        print("it is prime no.")




