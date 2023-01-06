def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x
def solution(w,h):
    answer = 0
    
    gNum = gcd(w,h)
    
    wN = w//gNum
    hN = h//gNum
    
    if w==1 or h==1:
        return 0
    
    if wN<hN:
        wN,hN=hN,wN
    
    
    if wN==hN:
        return w*h-wN*gNum
    else:
        return w*h-(w+h-gNum)
    

print(solution(8,7))