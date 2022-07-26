def solution(n, lost, reserve):
    i=0
    lost.sort()
    reserve.sort()
    gyo = set(lost) & set(reserve)
    for k in gyo:
        del lost[lost.index(k)]
        del reserve[reserve.index(k)]    
        
    while(i<len(lost)):
        if len(reserve)==0:
            break
        if lost[i]-1 in reserve:
            v = lost[i]
            del lost[lost.index(v)]
            del reserve[reserve.index(v-1)]
        elif lost[i]+1 in reserve:
            v = lost[i]
            del lost[lost.index(v)]
            del reserve[reserve.index(v+1)]            
        else:
            i+=1  
    return n-len(lost)  
