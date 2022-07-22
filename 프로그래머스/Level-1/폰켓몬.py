def solution(nums):
    answer = 0
    poketL = []
    
    for i in range(len(nums)):
        if nums[i] not in poketL:
            poketL.append(nums[i])
        
    if len(poketL) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(poketL)
    
