r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

board = [[0]*9 for i in range(10)]
visited = board

dx = [-2,2,3,3,2,-2,-3,-3]
dy = [-3,-3,-2,2,3,3,2,-2]
px = [-1,0,1,2,1,2,1,0,-1,-2,-1,-2]
py = [-2,-1,-2,-1,0,1,2,1,2,1,0,-1]

def dfs(x,y):
    count = 0
    co=0
    if visited[x][y]==0:
        count+=1
        visited[x][y]=1

    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        
        if xx<0 or yy<0 or xx>=10 or yy>=9:
            continue

        if visited[xx][yy]==1:
            co+=1
        if visited[xx][yy]==0:
            k = i+i//2
            check=0
            # for k in range(2):
            #     qx=x+px[k]
            #     qy=y+py[k]
            #     if qx!=r2 and qy!=c2:
            #         check+=1
            if check==2:
                print("@",xx,yy)
                if xx==r2 and yy==c2:
                    return count
                count += dfs(xx,yy)

        if co==8:
            return -1
    return count
print(dfs(r1,c1))
            
                    

