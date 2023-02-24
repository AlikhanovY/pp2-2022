

a=input()
import re
x=re.findall('[A-Z][^A-Z]*',a)
print(x)