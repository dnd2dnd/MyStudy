def solution(numbers):
    answer = 0
    nums = {0,1,2,3,4,5,6,7,8,9}
    
    gn = list(nums-set(numbers))
    
    for i in range(len(gn)):
        answer+=gn[i]

    return answer