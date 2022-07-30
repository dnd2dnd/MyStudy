def solution(n):
    answer = ''
    nums = [1,2,4]
    check = []
    
    while(n>0):
        n-=1
        check.append(nums[n%3])
        n//=3
    for i in range(len(check)-1,-1,-1):
        answer+=str(check[i])
    return answer


def solution1(n):
    answer = ''
    nums = ['1','2','4']
    
    while(n>0):
        n-=1
        answer=nums[n%3]+answer
        n//=3

    return answer