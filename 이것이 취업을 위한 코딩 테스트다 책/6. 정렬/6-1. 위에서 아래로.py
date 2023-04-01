n = int(input())
li = list()

for i in range(n):
    li.append(int(input()))

li.sort(reverse=True)

for i in li:
    print(i, end=' ')



