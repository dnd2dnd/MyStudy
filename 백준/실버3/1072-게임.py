from math import floor
x,y=map(int, input().split())
z=floor(100*y/x)
f,b=0,1000000000
if z>=99: print(-1)
else:
    while(f<=b):
        mid=(f+b)//2
        tx,ty=x+mid,y+mid
        if(floor(100*ty/tx)>z):
            b=mid-1
        else:
            f=mid+1
    print(b+1)
