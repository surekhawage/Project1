import os

print(os.getcwd())

#TO get the contents of sub directory also

# for dirpath,dirname,filenames in os.walk("Python projects/JulyPractice"):
#     print("Current directory path:",dirpath)
#     print("Directories:",dirname)
#     print("Files:",filenames)
#     print()

#To get the content of specified directory but not its sub directory

print(os.listdir("Python projects/JulyPractice"))

