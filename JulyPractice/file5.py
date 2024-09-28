import os, sys

fname = input("Enter file name:")

if os.path.isfile(fname):
    print("File eixts:",fname)
    f = open(fname,"r")
else:
    print("File doesn't exists:",fname)
    sys.exit(0)
Icount=wcount=ccount=0
for line in f:
    Icount = Icount+1
    ccount= ccount+len(line)
    words =line.split()
    wcount = wcount +len(words)
print("Number of  lines:",Icount)
print("number of words:",wcount)
print("Number of characters",ccount)

