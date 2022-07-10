n = int(input())

for i in range(1,2*n):
    if(i<=n):
        for k in range(i):
            print("*", end='')
        for j in range(n-i):
            print("  ", end='')
        for k in range(i):
            print("*", end='')
    else:
        for k in range(2*n-i):
            print("*", end='')
        for j in range(-n+i):
            print("  ", end='')
        for k in range(2*n-i):
            print("*", end='')
    print()