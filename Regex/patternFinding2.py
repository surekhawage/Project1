import re
def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'Match Found'
    else:
        return 'Match Not Found!'
    
print(text_match("aaa_bbb"))
print(text_match("AAA_Bbb"))
print(text_match("Aaa_bbb"))