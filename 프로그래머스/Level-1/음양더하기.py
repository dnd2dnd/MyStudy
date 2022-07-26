def solution(absolutes, signs):
    answer=0
    for i in range(len(absolutes)):
        print(signs[i], absolutes[i])
        if signs[i]:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer