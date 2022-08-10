import heapq
def solution(scoville, K):
    answer = 0
    li = list()
    for i in scoville:
        heapq.heappush(li, i)
    while(li[0]<K):
        if len(li)>1:
            a = heapq.heappop(li)
            b = heapq.heappop(li)
            c = a+(b*2)
            heapq.heappush(li, c)
            answer+=1            
        else:
            return -1
    return answer