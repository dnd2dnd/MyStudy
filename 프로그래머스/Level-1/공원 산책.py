def solution(park, routes):
    answer = []
    board = []
    now = []
    px = len(park)
    py = len(park[0])
    al = ["S","N","E","W"]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(len(park)):
        for k in range(len(park[i])):
            if park[i][k]=="S":
                now.append([i,k])
    
    for r in routes:
        move = r.split(' ')
        i = al.index(move[0])
        move[1] = int(move[1])
        X, Y = now[0][0]+dx[i]*move[1], now[0][1]+dy[i]*move[1]
        if X<0 or Y<0 or X>=px or Y>=py:
            continue
        
        check = True
        X, Y = now[0][0], now[0][1]
        for k in range(move[1]):
            X, Y = X+dx[i], Y+dy[i]
            if X<0 or Y<0 or X>=px or Y>=py or park[X][Y]=='X':
                check = False
                break
        if check:
            now[0][0], now[0][1] = now[0][0]+dx[i]*move[1], now[0][1]+dy[i]*move[1]
        
    answer.append(now[0][0])
    answer.append(now[0][1])

    return answer