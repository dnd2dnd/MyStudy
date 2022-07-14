def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    
    inter = set(str1_lst) & set(str2_lst)
    union = set(str1_lst) | set(str2_lst)
    gyo=0
    for x in inter:
        gyo += min(str1_lst.count(x),str2_lst.count(x))    
    hap=0
    for x in union:
        hap += max(str1_lst.count(x),str2_lst.count(x))
    if hap == 0 and gyo == 0:
        return 65536
    else:
        return int(gyo / hap * 65536)

print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))