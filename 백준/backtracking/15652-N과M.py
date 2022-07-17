n, m = map(int, input().split())

numL = []
def back(k):
    if len(numL)==m:
        print(' '.join(map(str, numL)))
        return

    for i in range(k, n+1):
        # print(i)
        if i not in numL or i==k:
            numL.append(i)
            back(k)
            numL.pop()
        k+=1

back(1)