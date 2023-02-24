import re

a=input()
x=re.findall(r"\B[a-z]+", a)
print(x)