def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    pn1, pn2, pn3 = 0,0,0
    for i in range(len(answers)):
        if person1[i%5]==answers[i]:
            pn1+=1
        if person2[i%8]==answers[i]:
            pn2+=1        
        if person3[i%10]==answers[i]:
            pn3+=1     
    
    maxNum = max(pn1,pn2,pn3)
    
    if maxNum<=pn1:
        answer.append(1)
    if maxNum<=pn2:
        answer.append(2)
    if maxNum<=pn3:
        answer.append(3)        
    return answer