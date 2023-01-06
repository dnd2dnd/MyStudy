def solution(numbers, target):
    answer = 0
    
    def dfs(hap, start):
        if start==len(numbers):
            if hap == target:
                nonlocal answer
                answer +=1
            return
        dfs(hap+numbers[start],start+1)
        dfs(hap-numbers[start],start+1)
    dfs(0,0)
    return answer

from collections import deque
def bfs(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer