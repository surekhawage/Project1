import re
text = "The Python are clike free easy to learn and open source language."
print(re.findall(r"\b\w{5}\b", text))
