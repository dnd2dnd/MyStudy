n, k = map(int, input().split())
thing = [[0,0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):    
    for j in range(1, k+1):
        weight = thing[i][0]
        value = thing[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
    for i in range(n+1):
        for j in range(k+1):
            print(dp[i][j] , end=' ')
        print()
    print()

print(dp[n][k])    
