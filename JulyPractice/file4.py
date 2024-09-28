import os,sys

fname = input("Enter file name:")

if os.path.isfile(fname):
    print("File exits:",fname)
    f = open(fname,"r")
else:
    print("File doesn't exists:",fname)
    sys.exit(0)
print("The content of file is :")
data = f.read()
print(data)

