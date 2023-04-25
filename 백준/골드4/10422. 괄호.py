# t = int(input())

# def sol(l):
#     if L==l:
#         return
#     for i in dp[l]:
#         if i+'()' not in dp[l+2]:
#             dp[l+2].append(i+'()')
#         if '()'+i not in dp[l+2]:
#             dp[l+2].append('()'+i)
#         if '('+i+')' not in dp[l+2]:            
#             dp[l+2].append('('+i+')')
#     sol(l+2)


# for i in range(t):
#     L = int(input())
#     if L%2==1:
#         print(0)
#     else:
#         dp = [[] for i in range(5001)]
#         dp[2] = ['()']
#         sol(2)
#         print(len(dp[L])%1000000007)


dp = [0 for _ in range(5001)]
dp[0] = 1

for n in range(2, 5001, 2):
    for i in range(2, n + 1, 2):
        dp[n] += dp[i - 2] * dp[n - i]
    dp[n] %= 1000000007

for _ in range(int(input())):
    print(dp[int(input())])