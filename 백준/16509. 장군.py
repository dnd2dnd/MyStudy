from collections import deque
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

board = [[0]*9 for i in range(10)]
visited = [[0]*9 for i in range(10)]

dy = [-2,2,3,3,2,-2,-3,-3]
dx = [-3,-3,-2,2,3,3,2,-2]
py = [-1,0,1,2,1,2,1,0,-1,-2,-1,-2]
px = [-2,-1,-2,-1,0,1,2,1,2,1,0,-1]


def bfs(x,y):
    queue = deque([])
    queue.append((x,y))
    
    while queue:
        count = 0
        x, y = queue.popleft()
        
        if x==r2 and y==c2:
            print(board[x][y])
            break

        for i in range(8):
            nx = x+ dx[i]
            ny = y+ dy[i]
            
            if nx < 0 or ny < 0 or nx>=10 or ny>=9:
                continue
            # print(nx,ny)
            if visited[nx][ny]==1:
                continue
            if visited[nx][ny]==0:
                key=i+(i//2)
                check = 0
                # if nx==2 and ny==5:
                for k in range(key, key+2):
                    qx, qy = x+px[k],y+py[k]
                    if qx==r2 and qy==c2:
                        check+=1
                if check==0:        
                    # print(nx, ny)
                    visited[nx][ny]=1
                    board[nx][ny]=board[x][y]+1
                    queue.append((nx,ny))

bfs(r1,c1)

