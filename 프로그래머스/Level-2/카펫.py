def solution(brown, yellow):
    yL=[]
    
    for i in range(1,yellow+1):
        if yellow%i==0:
            yL.append(i)
    
    for i in range(len(yL)):
        if (yL[-i-1]+2)*2+yL[i]*2==brown:
            return [yL[-i-1]+2, yL[i]+2]