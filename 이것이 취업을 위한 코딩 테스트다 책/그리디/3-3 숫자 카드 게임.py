n, m = map(int, input().split())

li = list()
for i in range(n):
    data = list(map(int, input().split()))
    li.append(min(data))

print(max(li))


