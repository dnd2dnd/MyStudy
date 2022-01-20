t=int(input())

def fac(m):
    sum=1
    for i in range(m,1,-1):
        sum*=i
    return sum

for i in range(t):
    n,m=map(int,input().split())
    print(fac(m)//fac(m-n)//fac(n))
