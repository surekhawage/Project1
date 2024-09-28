from zipfile import *

# To zipfile


f = ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("abc.txt")
f.write("abcde.txt")
f.write("bin1.txt")
f.close()
print("Zip file created and added files successfully")
