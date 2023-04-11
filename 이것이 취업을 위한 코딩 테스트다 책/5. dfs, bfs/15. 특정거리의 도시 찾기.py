from collections import deque

n, m, k, x = map(int, input().split())

li = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    li[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0
val=[]

def sol(graph, s):
    queue = deque([s])

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                queue.append(node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)