import re

def main():
    lower_case_pattern = re.compile(r'[a-z]')
    upper_case_pattern = re.compile(r'[A-Z]')
    number_pattern = re.compile(r'[0-9]')
    special_character_pattern = re.compile(r'[$@#]')

    password = input("Enter a password\n")

    if len(password)<8:
        print("Invalid Password. Length not Matching")
    elif not lower_case_pattern.search(password):
        print("Invalid Password. No Lower case letters")
    elif not upper_case_pattern.search(password):
        print("Invalid password. No Upper case letters")
    elif not number_pattern.search(password):
        print("Invalid Password. No Numbers")
    elif not special_character_pattern.search(password):
        print("Invalid Password. No special character")
    else:
        print("Valid Password")

if __name__=="__main__":
    main()



