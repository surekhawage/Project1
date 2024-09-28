print("To check whether your are going to sit in exam or not please enter the following:")
working = int(input("Total no. working days:"))
absent = int(input("Total no. of days for absent:"))

attendence = working - absent

present_percentage = attendence/working*100
eligible = working*75/100

if attendence >= eligible :
    print(f"Your total attendents is {present_percentage}%, so you can sit in exam")
else :
    print(f"Your total attendents is {present_percentage}%, so you cannot sit in exam")


