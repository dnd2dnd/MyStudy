n = int(input())
x, y = 1, 1

dataL = input().split()
move = {"L":-1, "R":1, "U":-1, "D":1}

for data in dataL:
    if(data=="L" or data=="R"):
        if((y+move[data]<1) or (y+move[data]>n)):
            continue
        y+=move[data]
    else:
        if((x+move[data]<1) or (x+move[data]>n)):
            continue
        x+=move[data]
print(x, y)

## 책 답안

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or  ny > n:
            continue
        x, y = nx, ny
print(x, y)