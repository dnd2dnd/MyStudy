from collections import deque

n = int(input())
board = []

for i in range(n):
    board.append(list(map(int, input())))

visited = [[0]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# DFS
# def dfs(x, y):
#     global cnt
#     visited[x][y]=1 
#     cnt+=1
#     for i in range(4):
#         xx, yy = x+dx[i], y+dy[i]

#         if xx<0 or yy<0 or xx>=n or yy>=n:
#             continue

#         if visited[xx][yy]==0 and board[xx][yy]==1:
#             dfs(xx, yy)
#     return cnt

# check = []
# cnt = 0

# for i in range(n):
#     for k in range(n):
#         if board[i][k]==1 and visited[i][k]==0:
#             check.append(dfs(i,k))
#             cnt=0

# check.sort()
# print(len(check))
# for v in check:
#     print(v)

count = 1
def bfs(x, y):
    global count
    queue = deque([(x, y)])
    board[x][y]=0
    while queue:
        now = queue.popleft()
        for i in range(4):
            X, Y = now[0]+dx[i], now[1]+dy[i]
            if X<0 or Y<0 or X>=n or Y>=n:
                continue

            if board[X][Y]==1:
                queue.append((X,Y))
                board[X][Y]=0
                count +=1

    return count

check = []
for x in range(n):
    for y in range(n):
        if board[x][y]==1:
            check.append(bfs(x,y))
            count=1

check.sort()
print(len(check))
for v in check:
    print(v)
           