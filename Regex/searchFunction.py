import re
str="I am indian,1947 mohit, mohitwage1@gamil.com wage"
result= re.search(r"Indian,1947 mohit",str,re.I)
result2= re.search(r"^I",str)
result3= re.search(r"wage$",str)
result4 = re.search(r"\w\w\w\w\w\w",str)
result5= re.search(r"\d\d\d\d",str)
result6= re.search(r"in\w+",str)
result7= re.search(r"\w+@\w+\.com",str)

print(result)
print(result.group())
print(result2.group())
print(result3.group())
print(result4.group())
print(result5.group())
print(result6.group())
print(result7.group())




