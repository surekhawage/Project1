import pickle

class Employee:
    def __init__(self,eno,ename,esal,addr):
        self.eno = eno;
        self.ename = ename;
        self.esal = esal;
        self.addr = addr;
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.addr)
with open("emp.dat","wb") as f:
    e =  Employee(100,"Mohit",10000,"Pune")
    pickle.dump(e,f)
    print("Pickling of employee Object completed")

with open("emp.dat",'rb') as f:
    obj = pickle.load(f)
    print("printing Employee information after unplicking")
    obj.display()
