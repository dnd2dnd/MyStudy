from itertools import permutations

def solution(numbers):
    answer = 0
    nL = [x for x in numbers]
    rnL = list()
    for k in range(1, len(numbers)+1):
        rnL += list(permutations(nL, k))
    new_nums = [int(("").join(p)) for p in rnL] 
    new_nums = list(set(new_nums))
    
    for num in new_nums:
        for i in range(2,num+1):
            if (i==num):
                answer+=1            
            if num%i==0:
                break
    return answer