import re
a=input()
x=re.sub(r"(\w)([A-Z])", r"\1 \2", a)
print(x)