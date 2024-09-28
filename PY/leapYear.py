year= input("Enter any year to check :")

num= int(year)%4
if(num==0):
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")