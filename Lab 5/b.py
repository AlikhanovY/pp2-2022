import re

a=input()
x=re.findall(r"\Bab{2,3}", a)
print(x)