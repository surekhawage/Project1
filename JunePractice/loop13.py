
password = str(input("Enter password to see its valid\n"))


if len(password) >=8 and len(password) <17 :

    has_upper = 0
    has_lower = 0
    has_digit = 0
    has_special = 0

    specail_character = "!@#$%^&*(),._?|-{}<>"

    for char in password :
        if char.isupper():
            has_upper = 1
        elif char.islower():
            has_lower = 1
        elif char.isdigit():
            has_digit = 1
        elif char in specail_character:
            has_special = 1
    
    if has_special+has_lower+has_digit+has_upper == 4:
        print("Password is valid")
        
    else:
        print("Password is invalid")
    
else:
    print("Password must be atleast 8 characters or 16 characters ")
