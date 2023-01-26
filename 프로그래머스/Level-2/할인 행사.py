def solution(want, number, discount):
    answer = 0
    
    fix = discount

    for i in range(len(fix)-9):
        discount = fix[i:i+10] 
        for k in range(len(want)):
            if (discount.count(want[k])<number[k]):
                break
            if (k==len(want)-1):
                answer+=1
        
        
    return answer