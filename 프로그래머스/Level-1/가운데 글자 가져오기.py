def solution(s):
    answer = ''
    
    k = len(s)//2
    if len(s)%2==0:
        return s[k-1:k+1]
    else:
        return s[k]
    return answer