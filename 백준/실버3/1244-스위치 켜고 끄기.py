total = int(input())
stateList = list(map(int, input().split()))
person = int(input())
for i in range(person):
    s, n = map(int, input().split())
    if s==1:
        for i in range(n,total+1,n):
            if stateList[i-1] == 0:
                stateList[i-1] = 1
            else:
                stateList[i-1] = 0
    elif s==2:
        k=1
        while(n-k-1>=0 and n+k-1<=total-1):
            if(stateList[n-k-1] == stateList[n+k-1]):
                if stateList[n-k-1] == 0:
                    stateList[n-k-1] = 1
                    stateList[n+k-1] = 1
                elif stateList[n-k-1] == 1:
                    stateList[n-k-1] = 0
                    stateList[n+k-1] = 0                
                k=k+1
            else:
                break
        if stateList[n-1] == 0:
            stateList[n-1] = 1
        else:
            stateList[n-1] = 0
for i in range(len(stateList)):
    print(str(stateList[i])+" ", end='')         
    if(i>1 and (i+1)%20==0):
        print()
