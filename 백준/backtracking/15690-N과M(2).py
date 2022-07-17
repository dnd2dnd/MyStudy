n, m = map(int, input().split())

numL = []
def back(i):
    if len(numL)==m:
        print(' '.join(map(str, numL)))
        return

    for i in range(i, n+1):
        if i not in numL:
            numL.append(i)
            back(i+1)
            numL.pop()


back(1)