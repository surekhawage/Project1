def moh(n):
    if n==0:
        result=1
    else:
        result= n*moh(n-1)
    return result



n = int(input("Enter number to see the factorial of that number"))
moh(n)
print(f"The factorial of {n} is {moh(n)}")


