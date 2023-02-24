import re

a=input()
x=re.findall(r"\B[ ,.]", a)
print(x)