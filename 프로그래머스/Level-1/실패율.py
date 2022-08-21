def solution(N, stages):
    answer = []
    sL = {}
    stages.sort()
    
    for i in range(1, N+1):
        count=0
        bl = len(stages)
        while(len(stages)>0):
            if i==stages[0]:
                stages.pop(0)
                count+=1
            else:
                break
        if bl==0:
            sL[i]=bl
        else:
            sL[i]=count/bl
            
    sort_sL = sorted(sL.items(), key = lambda item: item[1], reverse = True)
    for k,v in sort_sL:
        answer.append(k)
    return answer