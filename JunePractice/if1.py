
age = int(input("Enter your age to see  if you are eligible for voting or not\n"))

if age >=18 :
    print("You are eligible for voting")

elif age < 18:
    print("You are underaged to give a vote")

elif age > 80 :
    print("You are aged to give a vote")

else:
    print("You are not eligible for voting")

