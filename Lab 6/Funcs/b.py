a=input()
low=0
up=0
for i in a:
    if i.isupper():
        up+=1
    else:
        low+=1
print(f"Number of lowcase letters is {low} and number of uppercase numbers is {up}")