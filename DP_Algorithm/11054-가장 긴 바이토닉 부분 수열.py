n = int(input())

numL = list(map(int, input().split()))

dp = [[ 0 for _ in range(2) ] for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0][0], dp[n-1][1] = 1, 1
    else:
        max_dp=0
        for j in range(i):
            if max_dp < dp[j][0] and numL[j] < numL[i]:
                max_dp = dp[j][0]
            dp[i][0] = max_dp + 1
        max_dp=0
        for j in range(n-i,n):
            if max_dp < dp[j][1] and numL[j] < numL[n-i-1]:
                max_dp = dp[j][1]
            dp[n-i-1][1] = max_dp +1
max = 0
for i in range(n):
    if max < dp[i][0]+dp[i][1]:
        max = dp[i][0]+dp[i][1]
        print(max, dp[i][0]+dp[i][1])



