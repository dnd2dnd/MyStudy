n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for i in range(n):
    board.append(list(map(int, input().split())))
cnt=0
def dfs(x, y, d):
    global cnt
    if board[x][y]==0:       
        cnt+=1
        board[x][y]=2 
    check = 0
    for i in range(1,5):
        if d-i<0:
            dd=d-i+4
        else:
            dd= d-i
        xx = x+dx[dd]
        yy = y+dy[dd]
        if xx<0 or yy<0 or xx>=n or yy>=m or board[xx][yy]==1:
            continue

        if board[xx][yy]==0: 
            dfs(xx, yy, dd)
        else:
            check+=1 
    print(check)
    if check==4:
        xx = x+dx[(d+2)%4]
        yy = y+dy[(d+2)%4]
        print(board)
        print(" ")
        if xx<0 or yy<0 or xx>=n or yy>=m or board[xx][yy]==1:
            print(cnt)
        else:
            dfs(xx, yy, d)

dfs(x,y,d)
# for b in board:
#     print(*b)
