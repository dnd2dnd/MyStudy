def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    
    for i in range(len(d)):
        sum += d[i]
        if(sum> budget):
            sum-=d[i]
            answer = i
            break
        if(i==len(d)-1):
            answer = i+1
    return answer