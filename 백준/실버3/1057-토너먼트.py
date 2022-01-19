n,a,b=map(int,input().split())
round=0
check=True
if(a>b):
    a,b=b,a
while(n>0):
    round+=1
    k=1
    z=0

    for i in range(1,n+1,2):
        if((a%2==1) and (a+1==b)):
            n=-1
            check=False
            break
        elif(i==a or i+1==a):
            z+=1
            a=k
        elif(i==b or i+1==b):
            z+=1
            b=k
        if(z==2):
            break
        # print(i,a,b)
        k+=1
    t=n//2
    if(t%2==1):
        n-=1

if(check==False):
    print(round)
else:
    print(-1)

