n, m = map(int, input().split())
x, y, d = map(int, input().split())
place=list()

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(n):
    place.append(list(map(int, input().split())))

count = 0
check = 0
place[x][y]=2
while(True):
    d = (d+3)%4
    dx = x+direct[d][0]
    dy = y+direct[d][1]

    if dx<0 or dy < 0 or dx > n or dy > n:
        continue

    if place[dx][dy]==0:
        x, y = dx, dy
        check = 0 
        place[x][y] = 2
        count +=1
    else:
        check +=1

    if check==4:
        dx = x + direct[(d+2)%4][0]
        dy = y + direct[(d+2)%4][1]
        check=0
        if dx<0 or dy < 0 or dx > n or dy > n or place[dx][dy]==1:
            break
        count+=1
        x, y = dx, dy
    
print(count)    

    
## 답안
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있다면
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다라면
        else:
            break
        turn_time = 0

print(count)

