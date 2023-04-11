n, m, k, x = map(int, input().split())
li = [[]]
for i in range(m):
    li.append(list(map(int, input().split())))

def sol(graph, start):
    