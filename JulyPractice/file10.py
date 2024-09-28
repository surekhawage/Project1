from zipfile import *

#to unZipfile
f = ZipFile("files.zip",'r',ZIP_STORED)
names  = f.namelist()

for name in names:
    print("File name:",name)
    print("Content of the fie is:")
    f1 = open(name,'r')
    print(f1.read())
    print()
