import re

a=input()
x=re.findall(r"a.+b\Z", a)
print(x)