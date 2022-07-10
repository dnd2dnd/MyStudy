t = int(input())
dp = [0]*(t+1)

score = list()
for i in range(t):
    score.append(int(input()))
dp[0]=0
dp[1]=score[0]

for i in range(2,t+1):
    dp[i] = max(dp[i-3] + score[i-2] + score[i-1], dp[i-2] + score[i-1])
print(dp)


