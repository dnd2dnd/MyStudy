n = int(input())
line = list()
for i in range(n):
    line.append(list(map(int, input().split())))

line = sorted(line)
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[0] = 1
    else:
        max_dp=0
        for j in range(i):
            if max_dp < dp[j] and line[j][1] < line[i][1]:
                max_dp = dp[j]
        dp[i] = max_dp+1
# print(line)
# print(dp)
print(n-max(dp))

