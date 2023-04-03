n, m = map(int, input().split())
money = []
d=[10001]* 10001
d[0]=0
for i in range(n):
    money.append(int(input()))

for i in range(m+1):
    for mon in money:
        d[i+mon] = min(d[i+mon], d[i]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])


## 답안
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])