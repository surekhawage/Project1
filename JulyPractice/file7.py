import csv

with open("emp.csv","w",newline='') as f:
    w = csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADD"])
    n = int(input("Enter the number of employees:"))
    for i in range(n):
        eno = input("Enter Employee number:")
        ename = input("Enter the name of employee:")
        esal = input("Enter the salary of Employee:")
        eadd = input("Enter the address:")
        w.writerow([eno,ename,esal,eadd])
print("Total number of employees data written successfully")


