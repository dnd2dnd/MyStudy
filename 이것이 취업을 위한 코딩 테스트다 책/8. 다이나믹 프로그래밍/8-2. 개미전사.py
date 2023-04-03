n = int(input())

datam = list(map(int, input().split()))

d=[0]* 1001

for i in range(n):
    if i<2:
        d[i]= datam[i]
    else:        
        d[i] = max(datam[i], d[i-2]+datam[i])

print(d[n-1])


## 답안
dp = [0] * 100

dp[0] = datam[0]
dp[1] = max(datam[0], datam[1])

for i in range(2, n):
    d[i] = max(dp[i-1], d[i-2]+dp[i])

print(d[n-1])