import re
def text_match(text):
    patterns = '\Bz\B'
    if re.search(patterns, text):
        return 'Match Found'
    else:
        return('Match Not Found !')
    
print(text_match("We saw a Chimpanzee in the jungle."))
print(text_match("We saw a tiger in the jungle"))

    