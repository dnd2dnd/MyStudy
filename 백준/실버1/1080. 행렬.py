n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int, list(input()))))

for i in range(n):
    b.append(list(map(int, list(input()))))

def change(x, y):
    global cnt
    if x+3>n and y+3>m:
        return -1
    
    if a[x][y] != b[x][y]:
        for i in range(3):
            for k in range(3):
                if a[x+i][y+k] == 0: 
                    a[x+i][y+k] = 1
                elif a[x+i][y+k] == 1: 
                    a[x+i][y+k] = 0
        cnt+=1
cnt=0
for x in range(n-2):
    for y in range(m-2):
        change(x, y)

if a==b:
    print(cnt)
else:
    print(-1)