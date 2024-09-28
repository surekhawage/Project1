f1 = open("pic1.jpeg","rb")
f2 = open("pic2.jpg","wb")
bytes = f1.read()
f2.write(bytes)
print("New image is available with the name: pic2.jpg")

