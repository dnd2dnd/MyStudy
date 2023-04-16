# from collections import deque
# n, k = map(int, input().split())

# count = 0
# queue = deque([])
# queue.append([n])

# while queue:
#     for i in range(len(queue)):
#         value = queue.popleft()

#         if k in value:
#             print(count)
#             queue=[]
#             break

#         for val in value:
#             if val*2<=100000 or val-1>=0:
#                 queue.append([val-1, val+1, val*2])
#     count+=1

import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        print(q)
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            print(array[next_v], next_v)
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))
