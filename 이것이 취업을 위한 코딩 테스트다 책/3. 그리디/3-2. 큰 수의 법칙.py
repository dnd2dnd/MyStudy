n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

sum=0
for i in range(m):
    if(i%(k+1)==0):
        sum += data[-2]
    else:
        sum += data[-1]

print(sum)


## 시간초과 해결 방법

# 공통
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()

sum=0
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k + m%(k+1)

result = 0
result += count * first # 가장 큰 수더 하기
result += (m - count) * second

print(result)

print(sum)
