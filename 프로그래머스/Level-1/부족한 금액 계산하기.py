def solution(price, money, count):
    answer = -1

    don = 0
    for i in range(1,count+1):
        don+=(price*i)
    
    if (don-money)>0:
        return don-money
    else:
        return 0