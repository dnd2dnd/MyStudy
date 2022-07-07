n = int(input())
grapeL = [0]
for i in range(n):
    grapeL.append(int(input()))

# dp = [[0 for _ in range(3)] for _ in range(n+1)]
# for i in range(2, n+1):
#     dp[i][0] = dp[i-1][0]
#     if dp[i-1][1] == 1 and dp[i-1][2] == 1:
#         pass
#     else:
#         dp[i][2] = dp[i-1][1]
#         dp[i][0] = max(dp[i-2][0], dp[i-1][0]) + grapeL[i-1]
#         dp[i][1] = 1

dp = [0]*(n+1)
for i in range(1, n+1):
    if i==1:
        dp[1]=grapeL[1]
    elif i==2:  
        dp[2]=dp[i-1]+grapeL[2]
    else:
        dp[i] = max(dp[i-3]+grapeL[i-1]+grapeL[i], dp[i-2] + grapeL[i], dp[i-1])
print(max(dp))

        
