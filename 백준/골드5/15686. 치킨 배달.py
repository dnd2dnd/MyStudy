n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
home = []
chicken = []
for x in range(n):
    for y in range(n):
        if board[x][y]==1:
            home.append((x,y))
        elif board[x][y]==2:
            chicken.append((x,y))
sumL = []

for chi in chicken:    
    sum = []
    for ho in home:    
        sum.append(abs(chi[0]-ho[0]) + abs(chi[1]-ho[1]))
    sumL.append(sum)
sumL.sort()
print(sumL)
