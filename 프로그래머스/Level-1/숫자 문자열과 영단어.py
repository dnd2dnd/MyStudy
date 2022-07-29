def solution(s):
    answer = []
    eng = ""
    word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(s)):
        if (s[i].isdigit()):
            answer.append(s[i])
        else:
            eng+=s[i]
        if eng in word:
            answer.append(word.index(eng))
            eng = ""
    ans = ""            
    for e in answer:
        ans+=str(e)
    return int(ans)