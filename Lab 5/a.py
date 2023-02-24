import re

a=input()
x=re.findall(r"\Bab*", a)
print(x)