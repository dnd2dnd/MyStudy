n = int(input())
tri = [0]*(n+1)
for i in range(1,n+1):
    tri[i] = list(map(int, input().split()))
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]

dp[1]=tri[1]
for i in range(2,n+1):
    for k in range(i):
        if k==0:
            dp[i][k] = dp[i-1][k] + tri[i][k]    
        elif k==i-1:
            dp[i][k] = dp[i-1][k-1] + tri[i][k] 
        else:
            dp[i][k] = max(dp[i-1][k-1] + tri[i][k], dp[i-1][k] + tri[i][k])
print(max(dp[n]))

