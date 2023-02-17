def square(n,m):
    a=n
    while a<=m:
        yield a*a
        a+=1
n=int(input())
m=int(input())
for i in square(n,m):
    print(i)