#Lists Data Structure 
num= [20,30,50,90,80,70,10,40,60]

#Sorting to ascending in lists
num.sort()

#adding an element in lists
num.extend([100,110])
num.append(120)
num.insert(0,0)

#deleting an element in lists
num.pop(1)
del num[0]
num.remove(120)

#sum of all elements
Add= sum(num)
#reverse of list
# num.reverse()


for x in num:{
  print(x)
}

#list slicing with Step
y= num[0:6:1]  

print(num)
print("The sum of Elements in list 'num' is ")
print(Add)
print(num[:10])
print(len(num))
print(y)

