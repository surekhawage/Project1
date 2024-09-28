import csv

f = open("emp.csv",'r')
r = csv.reader(f)
data = list(r)

for line in data:
    for word in line:
        print(word,"\t",end='')
    print()

