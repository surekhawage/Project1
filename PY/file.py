f= open("r.txt","w")
f.write("Python Programming\n language")
f.close()
f= open("r.txt","r")
print(f.readline(100))
f.close()









# f= open("text.txt","r")
# line= f.readlines()
# print(line)
# f.close()