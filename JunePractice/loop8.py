

armstrong = []
for i in range(1,101):
    digits = 0  
    num_str= str(i)
    num_len= len(num_str)

    for num in num_str:
        digits += int(num)**num_len
    if i == digits:
        armstrong.append(i)
    
print(armstrong)

    