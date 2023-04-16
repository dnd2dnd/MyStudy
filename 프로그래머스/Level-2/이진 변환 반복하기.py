def solution(s):
    answer = []
    
    count1=0
    count0=0
    new = ''
    while True:
        if s =="1":
            break
        
        for i in s:
            if i=='1':
                new+=i
            else:
                count0+=1
            
        
        s = format(len(new), 'b')
        new=''
        count1+=1                
        
    answer.append(count1)
    answer.append(count0)
    return answer