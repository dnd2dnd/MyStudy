def solution(board, moves):
    answer = 0
    basket = []
    boardL = [[0 for i in range(len(board))] for k in range(len(board[0]))]
    for i in range(len(board)):
        for k in range(len(board[0])):
            boardL[i][k] = board[k][i]
    print(boardL)
    
    for i in moves:
        while(boardL[i-1]):
            k = boardL[i-1][0]
            if k!=0:
                basket.append(k)
                boardL[i-1].pop(0)
                break
            else:
                boardL[i-1].pop(0)                  
        if len(basket)>=2:
            if basket[-1]==basket[-2]:
                basket.pop(-1)
                basket.pop(-1)
                answer+=2
             
    return answer