n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    board.append(list(map(int, input().split())))
cnt=0
def dfs(x, y, d):
    global cnt
    if board[x][y]==0:       
        cnt+=1
        board[x][y]=2
    check=0
    for i in range(4):
        dd=(d+3-i)%4
        xx, yy = x+dx[dd], y+dy[dd]
        if xx<0 or yy<0 or xx>=n or yy>=m:
            continue

        if board[xx][yy]==0: 
            dfs(xx, yy, dd)
        else:
            check+=1

    if check==4:
        xx = x+dx[(d+2)%4]
        yy = y+dy[(d+2)%4]
        if xx>=0 and yy>=0 and xx<n and yy<m:
            print(board[xx][yy], xx, yy)
            if board[xx][yy]!=1:
                dfs(xx, yy, d)    
            else:
                print(cnt)
                exit(0)
            
dfs(x,y,d)
