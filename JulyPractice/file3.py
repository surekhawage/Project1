data = "Hey i am Mohit"
f= open("bin1.txt",'w')    
f.write(data)

with open("bin1.txt",'r+') as f:
    r1 = f.read()
    print(r1)
    print("The current position of cursor:",f.tell())
    f.write(" Wage!")
    f.seek(0)
    r1 = f.read()
    print("Data after modification:")
    print(r1)

