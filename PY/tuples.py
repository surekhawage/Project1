# assignment of tuple
ID= ("Mohit", 22, "udgir")
(name, age, city) =ID
print(name,age,city)


#deleting an element from tuple by converting it to lists and then again back to tuple
age= (20,21,22,23,24,25)
j= list(age)
del j[2]
print(j)

OL= tuple(j)
print(OL)

#we update an element in a tuple only in nested items
decimal= (0,1,2,3,[4,5],6,7,8,9)
decimal[4][0]=11
decimal[4][1]=12
print(decimal)
#or by coverting a tuple in to a list and then again back to a tuple

#concatenation and repetation of tuples
a=('a','b','c','d')
b= ('e','f','g','h')
print(a+b)
print(a*2)

#membership funtion
s= 1.0,2.0,3.0,4.0,5.0
flag=1.0 in s
print(flag)

#iteration through a tuple
years= 2023,2024,2025,2026
for x in years:{
    print(x)
}