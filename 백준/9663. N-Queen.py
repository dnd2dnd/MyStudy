n = int(input())

board = [[0 for j in range(n)] for i in range(n)]
visited = [[0 for j in range(n)] for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def check(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    
def queen(x, y):
    check(x, y)

    if visited[x][y]==1:
        return False
    else:
        visited[x][y]=1
        
        # x축 y축 1로 넣기
        for i in range(n):
            visited[x][i]=1
            visited[i][y]=1

        # 1사분면
        cx, cy = x, y
        for i in range(x,0, -1):
            visited[cx][cy]=1
            cx-=1
            cy-=1
            if check(cx,cy)==False:
                break

        # 2사분면
        cx, cy = x, y
        for i in range(x,0, -1):
            visited[cx][cy]=1
            cx+=1
            cy-=1
            if check(cx,cy)==False:
                break


        # 3사분면
        cx, cy = x, y
        for i in range(x,n):
            visited[cx][cy]=1
            cx-=1
            cy+=1
            if check(cx,cy)==False:
                break
          

        # 4사분면
        cx, cy = x, y
        for i in range(x,n):
            visited[cx][cy]=1
            cx+=1
            cy+=1    
            if check(cx,cy)==False:
                break

        return True

count = 0
for i in range(n)                                        :
    for k in range(n):
        if queen(i,k):
            print(i, k)
            count +=1
print(count)
        