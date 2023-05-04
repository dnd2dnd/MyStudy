import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())

board = [[ 0 for _ in range(N)] for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    board[x][y]=1
    cnt+=1

    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx<0 or yy<0 or xx>=M or yy>=N or board[xx][yy]==1:
            continue

        dfs(xx,yy)

for i in range(K):
    y1, x1, y2, x2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y]=1


cntL = []
for x in range(M):
    for y in range(N):
        if board[x][y]==0:
            cnt = 0
            dfs(x, y)
            cntL.append(cnt)

print(len(cntL))
cntL.sort()
print(*cntL)

    