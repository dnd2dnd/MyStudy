def checkPlace(place):
    pList = []
    for x in range(5):
        for y in range(5):
            if place[x][y]=='P':
                pList.append((x, y))

    for x, y in pList:
        for x2, y2 in pList:
            d = abs(x-x2)+abs(y-y2)
            if d==0 or d>2:
                continue
            if d==1:
                return 0
            elif x==x2 and place[x][int((y+y2)/2)]!='X':
                return 0
            elif y==y2 and place[int((x+x2)/2)][y]!='X':
                return 0
            elif x!=x2 and y!=y2:
                if place[x2][y] != 'X' or place[x][y2] != 'X':
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(checkPlace(place))

    return answer