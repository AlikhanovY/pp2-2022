def even(n):
    a=1
    while a <= n:
        if(a%2==0):
            yield f"{a},"
        a+=1
n=int(input())
str=""
for i in even(n):
    str=str+i

print(str)