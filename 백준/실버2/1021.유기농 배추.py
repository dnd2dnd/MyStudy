import sys
sys.setrecursionlimit(10000)

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    board[x][y]=0

    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx<0 or yy<0 or xx>=N or yy>=M or board[xx][yy]==0:
            continue
        dfs(xx, yy)

    
for i in range(T):
    M, N, K = map(int, input().split())    
    board = [[ 0 for j in range(M)] for i in range(N)]
    count = 0

    for _ in range(K):
        a, b = map(int, input().split())
        board[b][a] = 1
    
    for x in range(N):
        for y in range(M):
            if board[x][y]==1:
                dfs(x, y)
                count+=1
    print(count)
         
