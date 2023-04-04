n, m = map(int, input().split())
data=[]
for i in range(m):
    data.append(list(input()))

visited = [[0 for col in range(n)] for row in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, value):
    count=0
    if visited[x][y]==0:
        visited[x][y]=1
        count+=1
    for i in range(4):    
        xx, yy = x+dx[i], y+dy[i]
        if xx<0 or yy<0 or xx>=m or yy>=n:
            continue
        if data[xx][yy]==value and visited[xx][yy]==0:
            count += dfs(xx,yy,value)
    
    return count


sum = 0
w=b=0

for i in range(m):
    for k in range(n):
        if data[i][k]=='W':
            w+=dfs(i,k,'W')**2
        else:
            b+=dfs(i,k,'B')**2
print(w,b)        




