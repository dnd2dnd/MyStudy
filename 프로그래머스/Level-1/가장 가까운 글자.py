def solution(s):
    answer = []
    eng = {'a':-1, 'b':-1, 'c':-1, 'd':-1, 'e':-1, 'f':-1, 'g':-1, 'h':-1, 'i':-1, 'j':-1
          , 'k':-1, 'l':-1, 'm':-1, 'n':-1, 'o':-1, 'p':-1, 'q':-1, 'r':-1, 's':-1, 't':-1
          , 'u':-1, 'v':-1, 'w':-1, 'x':-1, 'y':-1, 'z':-1}
    
    for i in range(len(s)):
        if eng[s[i]]==-1:
            answer.append(-1)
        else:
            answer.append(i-eng[s[i]])
        eng[s[i]]=i    
        
    return answer


def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer    