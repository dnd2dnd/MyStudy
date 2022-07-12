n = int(input())

numL = list(map(int, input().split()))
dp=[0] * n
for i in range(n):
    if i == 0:
        dp[0] = 1 
    else:
        max_dp = 0
        for j in range(0, i):
            if max_dp < dp[j] and numL[j] < numL[i]:
                max_dp = dp[j]
        dp[i] = max_dp+1

print(dp)

