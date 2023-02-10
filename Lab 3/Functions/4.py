import math
def prime(num):
    prime=[]
    c=0
    for i in num:
        for d in range(2,int(math.sqrt(i))):
            if i%d == 0:
                c=c+1
                break
        if c==0:
            prime.append(i)
        c=0
    return prime
num = list(map(int, input().split()))
print(prime(num))


