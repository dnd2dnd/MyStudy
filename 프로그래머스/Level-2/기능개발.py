import math
def solution(progresses, speeds):
    answer = []
    ch = []
    for i in range(len(progresses)):
        ch.append(math.ceil((100-progresses[i])/speeds[i]))

    while(len(ch)>0):
        x = ch[0]
        sum = 1
        i=1
        while(True):
            if len(ch)==1:
                answer.append(sum)
                ch.pop(0)
                break
            else:
                if x>=ch[i]:
                    sum+=1
                    ch.pop(0)              
                else:
                    ch.pop(0)
                    answer.append(sum)
                    break
                    
    return answer