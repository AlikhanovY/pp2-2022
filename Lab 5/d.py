import re

a=input()
x=re.findall(r"\B[A-Z]{1}[a-z]+", a)
print(x)