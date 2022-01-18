t=int(input())
hang=list()

for i in range(0,t):
    startA,startB,endA,endB=map(int,input().split())
    n=int(input())
    cnt=0
    for k in range(0,n):
        x,y,r=map(int,input().split())
        start_pos=(x-startA)**2+(y-startB)**2
        end_pos=(x-endA)**2+(y-endB)**2
        if(start_pos<r**2 and end_pos<r**2):
            pass
        elif(start_pos<r**2):
            cnt+=1
        elif(end_pos<r**2):
            cnt+=1
    print(cnt)