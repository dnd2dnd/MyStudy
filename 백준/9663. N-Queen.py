n = int(input())

board = [[0 for j in range(n)] for i in range(n)]
visited = [[0 for j in range(n)] for i in range(n)]

def check(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return
    
def queen(x, y):
    check(x, y)

    if visited[x][y]==1:
        return
    else:
        visited[x][y]=1
        dx, dy = x, y
        for i in range(x,n):
            visited[dx][dy]=1
            dx+=1
            dy+=1
        for i in range(x,0, -1):
            pass