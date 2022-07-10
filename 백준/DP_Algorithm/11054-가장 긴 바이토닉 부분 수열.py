n = int(input())

numL = list(map(int, input().split()))
maxNum = max(numL)
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[0] = 1
    else:
        for j in range(0, i):
            max_dp=0
            min_dp=1001
            if numL[i] == maxNum:
                if min_dp > dp[j] and numL[j] < numL[i]:
                    min_dp = dp[j]
                dp[i] = min_dp+1
            else:
                if max_dp < dp[j] and numL[j] < numL[i]:
                    max_dp = dp[j]
                dp[i] = max_dp+1

print(dp)

