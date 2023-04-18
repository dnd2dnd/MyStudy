t = int(input())

for i in range(t):
    cnt = 1
    di = dict()
    n = int(input())
    for k in range(n):
        str = input().split()
        if str[1] in di:
            di[str[1]].append(str[0])
        else:
            di[str[1]] =[str[0]]

    for z in di:
        cnt *= (len(di[z])+1)
    print(cnt-1)