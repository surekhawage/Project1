import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):
    if(re.search(regex,email)):
        print('Valid Mail Address')
    else:
        print('Invalid Mail Address')
    
if __name__=='__main__' :
    email= input("Enter E-mail\n")
    check(email)
