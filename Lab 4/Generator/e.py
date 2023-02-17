def tozero(n):
    a=n
    while(a>=0):
        yield a
        a-=1
n=int(input())
for i in tozero(n):
    print(i)