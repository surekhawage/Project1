class TooOldException(Exception):
    def __init__(self,arg):
        self.msg = arg
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg = arg

age = int(input("Enter your age:"))

if age>60:
    raise TooOldException("Your age has gone to get married")
elif age<18:
    raise TooYoungException("Your age is not to get married")
else:
    print("you will get email")

