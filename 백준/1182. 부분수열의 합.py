from itertools import combinations

n, s =map(int, input().split())
li = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    result = list(combinations(li,i))
    for val in result:
        if sum(val)==s:
            count+=1

print(count)
