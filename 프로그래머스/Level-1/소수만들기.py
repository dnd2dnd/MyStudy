def solution(nums):
    answer=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                check=0
                for z in range(1,nums[i]+nums[j]+nums[k]):
                    if ((nums[i]+nums[j]+nums[k])%z==0):
                        check+=1
                if (check==1):
                    answer+=1
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
