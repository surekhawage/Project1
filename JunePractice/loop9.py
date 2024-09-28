print("Enter the range from Start to end to display the even numbers\n")
start = int(input("Start"))
end = int(input("End"))

even = []

for i in range(start,end):
    if i %2==0:
        even.append(i)
    else:
        continue

print(even)

