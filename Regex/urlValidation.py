import re
def checkurl(str):
    regex = ("((http|https)://)(www.)?"+
             "[a-zA-Z0-9@:%._\\+~#?&//=]"+
             "{2,256}\\.[a-z]"+
             "{2,6}\\b([-a-zA-Z0-9@:%"+"._\\+~#?&//=]*)")
    p = re.compile(regex)
    if(str==None):
        return False
    if(re.search(p,str)):
        return True
    else:
        return False
    
if __name__=='__main__':
    url = input("Enter URL")
    if(checkurl(url)==True):
        print("Valid URL")
    else:
        print("Invalid URL")
        