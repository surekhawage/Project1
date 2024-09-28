percentage = float(input("Enter your percentage to see your grade:\n"))

if percentage >90:
    print(f"The percentage of {percentage}, Grade : A", )
elif percentage >80 <=90:
    print(f"The percentage of {percentage}, Grade : B", )
elif percentage >=60 <=80:
    print(f"The percentage of {percentage}, Grade : C", )
elif percentage <60 :
    print(f"The percentage of {percentage}, Grade : D", )

