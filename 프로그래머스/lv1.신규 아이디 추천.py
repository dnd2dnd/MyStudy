def solution(new_id):
    characters="~!@#$%^&*()=+[{]}:?,<>/"
    print(characters[-1])
    #1단계
    new_id=new_id.lower()
    print(new_id)
    #2단계
    for i in range(len(characters)):
        new_id=new_id.replace(characters[i],"")
    if(len(new_id)==0):
        new_id='a'
    print(new_id)
    #3단계
    for i in range(len(new_id)-1):
        new_id=new_id.replace("..",".")
    if(len(new_id)==0):
        new_id='a'
    print(new_id)
    #4단계
    if new_id[0]=='.':
        new_id=new_id[1:len(new_id)]
    if(len(new_id)==0):
        new_id='a'
    if new_id[-1]=='.':
        new_id=new_id[0:len(new_id)-1]
    if(len(new_id)==0):
        new_id='a'
    print(new_id)
    #5단계
    new_id=new_id.replace("..","")
    if(len(new_id)==0):
        new_id='a'
    print(new_id)
    #6단계
    if(len(new_id)>=16):
        new_id=new_id[0:15]
    if new_id[-1]=='.':
        new_id=new_id[0:len(new_id)-1]
    print(new_id)
    #7단계
    while(True):
        if len(new_id)<=2:
            new_id+=new_id[-1]
        else:
            break
    print(new_id)
    
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))