def fac(a):
    sum=0
    for i in range(1,a):
        sum+=i
    return sum

n,l=map(int,input().split())
al=list()
a=0
b=0
for i in range(l,101):
    if (n-fac(i))%i==0 and (n-fac(i))//i>=0:
        a=(n-fac(i))//i
        b=i
        break
if b==0 or b>100:
    print(-1)
else:
    for i in range(b):
        print(a+i)

