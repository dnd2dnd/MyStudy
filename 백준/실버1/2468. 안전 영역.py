import sys
sys.setrecursionlimit(10**6)

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
check = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, n):

    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]

        if xx<0 or yy<0 or xx>=N or yy>=N or check[xx][yy]==1:
            continue

        if board[xx][yy]>n and check[xx][yy]==0:
            check[xx][yy]=1
            dfs(xx, yy, n)

maxC = 1
mV = max(max(board))+1
for i in range(mV):
    check = [[0 for _ in range(N)] for _ in range(N)]
    cnt=0
    for x in range(N):
        for y in range(N):
            if board[x][y]>i and check[x][y]==0:
                dfs(x, y, i)
                cnt+=1
    if maxC < cnt:
        maxC = cnt

print(maxC)