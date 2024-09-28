import file16
import pickle

f = open("emp.dat",'wb')
n = int(input("Enter the no. employees"))

for i in range(n):
    eno = int(input("Enter the employee no.:"))
    ename = input("Enter employee name:")
    esal = float(input("Enter salary"))
    eaddr = input("Enter address")
    e = file16.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
print("Employee objects pickled successfully ")


