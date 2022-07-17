n, m = map(int, input().split())
numL=[]
def back(m,numL=[]):
    if m==0:
        print(' '.join(map(str, numL)))
        return
    for i in range(1, n+1):
        if i not in numL:
            numL.append(i)
            back(m-1, numL)
            numL.pop()
back(m)
