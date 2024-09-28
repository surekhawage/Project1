m1= int(input("Enter marks of subject 1 :"))
m2= int(input("Enter marks of subject 2 :"))
m3= int(input("Enter marks of subject 3 :"))

total= m1+m2+m3
per= total/3

print("The Total Marks obtain :",total)
print("The percentage is :", per)

if(per>=75):
    print("Distinction")
elif(per>=60 and per<75):
    print("First class")
elif(per>=45 and per<60):
    print("Second class")
elif(per>=40 and per<45):
    print("Pass")
else:
    print("Fail")    



    
