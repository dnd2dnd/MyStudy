n, m = map(int, input().split())

numL = []

def back():
    if len(numL)==m:
        print(' '.join(map(str, numL)))
        return

    for i in range(1, n+1):
        numL.append(i)
        back()
        numL.pop()

back()