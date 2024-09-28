num1= [1,2,3,4,5,6,7,8,9]
value= int(input("Enter any number you want from the list \t"))


def linear_search(list,want):

    for x in range(0,len(list)):
        
        if(num1[x]==want):
            print("The item u wanted is :", want)
            break
            
        else:
            print("THe item you want is not in the list")

linear_search(num1,value)