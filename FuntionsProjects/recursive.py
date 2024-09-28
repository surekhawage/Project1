def addition(*numbers):

    A= 0
    for i in numbers:
        
        A= A+i

        if(numbers==0):

            break
        print(A)
    
numbers= [1,2,3,4,5,6,7,8,9]

addition(numbers)

