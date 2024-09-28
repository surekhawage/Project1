kilometers = int(input("Enter the total kilometers\n"))

if kilometers <=10:
    print(f"The bill of  kilometer :{kilometers} is :", kilometers*11)
elif kilometers >10 and kilometers <=90:
    after_10km = kilometers - 10
    next_90km = 110 + after_10km*10
    print(f"The bill of kilometer:{kilometers} is:", next_90km)
elif kilometers >90:
    after_90km = kilometers - 90
    after_90kms = 110 + 800 +after_90km*9
    print(f"The bill of kilometer :{kilometers} is :",after_90kms)
else:
    print("Please enter valid number of km")


