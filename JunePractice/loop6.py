# prime =[]

# for i in range (1,101):
#     for num in range(2,i):
#         if i%num==0:
#             break
#     else:
#         prime.append(i)

# print(prime)


prime = []

for i in range(1,101):
    for num in range(2,i):
        if i%num==0:
            break
    else :
        prime.append(i)

print(prime)

    