import re
str= "Hey Mohit Pandharinath Wage"
result= re.match(r"hey",str,re.I)
print(result)
print(result.group())
print(result.groups())
print(result.start())
print(result.end())
print(result.span())

