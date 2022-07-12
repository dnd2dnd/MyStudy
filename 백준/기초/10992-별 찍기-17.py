n = int(input())

for i in range(1,n+1):
    if i==n:
        for z in range(2*n-1):
            print("*",end='')
    else:
        for k in range(n-i):
            print(" ", end='')
        print("*", end='')
        for k in range(2*(i-1)-1):
            print(" ", end='')
            if k==2*(i-1)-2:
                print("*",end='')
        print()

