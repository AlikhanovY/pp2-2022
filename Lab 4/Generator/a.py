
def sq(n):
    a=1
    while a <= n:
        yield a*a
        a=a+1
n=int(input())
for i in sq(n):
    print(i)