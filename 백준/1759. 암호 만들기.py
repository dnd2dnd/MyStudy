from collections import deque
moeum = ['a','e','i','o','u']

l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
answer = []

def dfs(v, c1, c2, str):
    if len(str)==l:
        if c1==0 and c2==0 and str not in answer:
            answer.append(str)
        return

    for i in range(v, len(alpha)):
        if alpha[i] not in str:
            if alpha[i] in moeum:
                dfs(i+1,c1-1, c2, str+alpha[i])
            else:
                dfs(i+1,c1, c2-1, str+alpha[i])

for i in range(1, l-1):
    dfs(0, i, l-i, '')

answer.sort()
for i in answer:
    print(i)