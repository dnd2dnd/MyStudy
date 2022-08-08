def solution(a, b):
    answer = ''
    date = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    d = 0
    for i in range(a-1):
        d+=day[i]
    
    return date[((d+b)%7)-1]