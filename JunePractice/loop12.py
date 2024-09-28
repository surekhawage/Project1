word = str(input("Enter any word to get it reversed\n"))

reverse = ""
for i in word:
    reverse = i +reverse

print(f"The reverse of word {word} is :{reverse}")

