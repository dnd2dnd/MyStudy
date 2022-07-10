n = int(input())

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    for z in range(i-1):
        print('*', end='')
    print()