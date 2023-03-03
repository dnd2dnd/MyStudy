import sys
from collections import Counter

n = int(input())
arr = [0] * 500000
li=list()
sum = 0
for i in range(n):
    a = int(sys.stdin.readline())
    sum += a
    li.append(a)

li.sort()
cnt = Counter(li).most_common(2)

print(round(sum/n))
print(li[len(li)//2])
if len(li) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(li[-1] - li[0])
