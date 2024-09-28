import re

ip1 = "989.001.878"
ip2 = "678.345.000"

string1= re.sub('\.[0]*', '.',ip1)
string2= re.sub('\.[0]*', '.',ip2)
print(string1)
print(string2)


