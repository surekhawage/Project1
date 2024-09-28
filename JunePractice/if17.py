print("Enter the age of any four persons to see who is youngest one")
person1 = int(input("Person 1 age:"))
person2 = int(input("Person 2 age:"))
person3 = int(input("Person 3 age:"))
person4 = int(input("Person 4 age:"))

if person1 < person2 and person1 < person3 and person1 < person4:
    print(f"Person 1 of age {person1} is the youngest one")
elif person2 < person1 and person2 < person3 and person2 < person4:
    print(f"Person 2 of age {person2} is the youngest one")
elif person3 < person1 and person3 < person2 and person3 < person4:
    print(f"Person 3 of age {person3} is the youngest one")
elif person4 < person1 and person4 < person2 and person4 < person3:
    print(f"Person 4 of age {person4} is the youngest one")

