import re
phone_check = re.compile(r"[^0-9s.]")
phone = input("Please enter your phone:")
while phone_check.search(phone):
    print("Please enter phone correctly")
    phone= input("Please, enter your phone:")
    