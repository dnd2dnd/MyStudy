def fib(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fib(n-1) + fib(n-2)

def dpfib(n):
    dp=[0]*(n+1)
    dp[0], dp[1] = 1, 1
    cnt=0
    for i in range(3,n+1):
        cnt+=1
        dp[i] = dp[i-1]+dp[i-2]
    return cnt

n = int(input())
print(fib(n),dpfib(n))