alpha= {1:"A",2:"B",3:"C",4:"D",5:"E"}
num= {1:10,2:20,3:30,4:40,5:50}
colors= dict([(1,"red"),(2,"blue"),(3,"yellow"),(4,"white"),(5,"orange")])

print(alpha)
print(num)
print(colors)

#accessing values in Diectionary
x= alpha[1]
y= num[2]
z= colors[3]
x1= alpha.get(6)


print(x)
print(y)
print(z)
print(x1)

#deleting element from the dictionary
del colors[5]
print(alpha.pop(3))
print(num.popitem()) #deletes the last item in the dictionary inserted in it
print(colors)

#updating an element in dictionary
alpha[6]='F'
colors[6]='pink'
print(alpha)
print(colors)

#all keys and values to print
a1= alpha.keys()
b1= colors.values()
print(a1)
print(b1)

#updating
p1= {1:10,2:20}
l1= {4:40,5:50}
p1.update(l1)
print(p1)








