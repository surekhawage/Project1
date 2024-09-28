import re

text = 'Python Program, Java Programming, Perl Programming'
pattern = 'Program'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' %(text[s:e], s,e))
    