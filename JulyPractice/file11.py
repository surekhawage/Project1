import os

#To know the current working directory:

cwd = os.getcwd()
print("The current working directory is :",cwd)

#To create sub directory:

# os.mkdir("mysub")
# print("mysub directory created")

#To create sub directory of mysub:

# os.mkdir("mysub/mysub2")
# print("mysub2 created inside in mysub")

#To create multiple directories

#os.makedirs("mysub/mysub1/mysub2/mysub3")
# print("All three directories created")


#To remove sub directory

# os.rmdir("mysub/mysub2")
# print("The mysub2 directory deleted")


#To remove multiple directories

# os.removedirs("mysub1/mysub2/mysub3")
# print("All 3 directories mysub1,mysub2,mysub3 removed")

#To rename a directory

# os.rename("mysub","maindirectory")
# print("Renamed the 'mysub'directory to 'maindirectory' ")


