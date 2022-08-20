def solution(s):
    answer = True
    aList = []
    
    if s[0]==")":
        return False
    if len(s)/2!=s.count("("):
        return False
    
    for i in s:
        if i == '(':
            aList.append(')')
        else:
            if aList:
                aList.pop()
            else:
                return False               
    if aList:
        return False

    return True