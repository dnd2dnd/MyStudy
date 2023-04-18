from itertools import combinations
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
# print(chicken)
chicken = list(combinations(chicken, m))
# print(chicken)

    
result = 1e9
for chi in chicken:
    sum = 0
    for ho in home:
        minV = 10000000
        for x in chi:
            minV = min(minV, abs(x[0]-ho[0]) + abs(x[1]-ho[1]))
        sum += minV
    result = min(result, sum)
print(result)    
