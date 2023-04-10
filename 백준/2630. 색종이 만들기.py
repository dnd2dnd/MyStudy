n = int(input())
board=[]
for i in range(n):
    board.append(list(map(int, input().split())))
vistied = [[0]* n for i in range(n)]
blue=0
white=0

def sol(x, y, n):
    global blue
    global white
    if n<1:
        return
    
    if(vistied[x][y]==1):
        return

    val = board[x][y]  

    check = 0 

    for i in range(x, x+n):
        for k in range(y, y+n):
            if board[i][k] == val:
                check+=1
    if check==n**2:
        if val==1:
            blue+=1
        else:
            white+=1
        for i in range(x, x+n):
            for k in range(y, y+n):        
                vistied[i][k]=1
    sol(x, y, n//2)
    sol(x+n//2, y, n//2)
    sol(x, y+n//2, n//2)
    sol(x+n//2, y+n//2, n//2)
    

sol(0,0, n)


print(white)
print(blue)