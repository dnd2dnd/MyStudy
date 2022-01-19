n,m=map(int,input().split())
al=list()

for i in range(n):
    al.append(list(map(int,input())))
minNum=min(n,m)
maxNum=max(n,m)

ans=0
for i in range(n):
    for k in range(m):
        for z in range(1,minNum):
            if((i+z<=n-1) and (k+z<=m-1)):
                if(al[i][k]==al[i][k+z]==al[i+z][k]==al[i+z][k+z]):
                    ans=max(ans,z+1)

if(ans==0):
    print(1)
else:
    print(ans**2)

