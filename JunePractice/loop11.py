word = str(input("Enter any word to check whether it is a palindrome or not\n"))

reverse = ""

for i in word:
    reverse = i + reverse 

if reverse == word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

