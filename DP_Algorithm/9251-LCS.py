a = input()
b = input()

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(len(b)):
    for k in range(len(a)):
        if a[k] == b[i]:
            if i==0:
                dp[i+1][k+1] = dp[i][k]+1
            else:
                dp[i+1][k+1] = dp[i][k]+1
        else:
            dp[i+1][k+1] = max(dp[i][k+1], dp[i+1][k])

print(max(max(dp)))