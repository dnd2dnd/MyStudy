# def solution(record):
#     answer = []
#     setid=set()
#     userid=[]
#     for i in range(len(record)):
#         temp=record[i].split(' ')
#         if temp[1] not in setid:
#             setid.add(temp[1])
#             userid.append([temp[1],temp[2]])
#         if temp[0]=="Enter":
#             for k in range(len(userid)):
#                 if temp[1] in userid[k]:
#                     userid[k][1]=temp[2]
#             answer.append(temp[1]+"님이 들어왔습니다.")
#         elif temp[0]=="Leave":
#             answer.append(temp[1]+"님이 나갔습니다.")
#         elif temp[0]=='Change':
#             for k in range(len(userid)):
#                 if temp[1] in userid[k]:
#                     userid[k][1]=temp[2]
#     for i in range(len(answer)):
#         for k in range(len(userid)):
#             answer[i]=answer[i].replace(userid[k][0],userid[k][1])
#     # print(userid)
#     # print(answer)
#     return answer

# def solution(record):
#     answer = []
#     setid=set()
#     userid={}
#     for i in range(len(record)):
#         temp=record[i].split(' ')
#         setid.add(temp[1])
#         if temp[0]=="Enter":
#             userid[temp[1]]=temp[2]
#             answer.append(temp[1]+"님이 들어왔습니다.")
#         elif temp[0]=="Leave":
#             answer.append(temp[1]+"님이 나갔습니다.")
#         elif temp[0]=="Change":
#             userid[temp[1]]=temp[2]
#     setid=list(setid)
#     for i in range(len(answer)):
#         for k in range(len(setid)):
#             answer[i]=answer[i].replace(setid[k],userid[setid[k]])            
#     # print(userid)
#     # print(answer)
#     return answer

def solution(record):
    answer = []
    setid=set()
    userid={}
    for i in range(len(record)):
        temp=record[i].split(' ')
        if len(temp)==3:
            userid[temp[1]]=temp[2]
    print(userid)            
    for i in range(len(record)):
        temp=record[i].split(' ')
        if temp[0]=="Enter":
            answer.append(userid[temp[1]]+"님이 들어왔습니다.")
        elif temp[0]=="Leave":
            answer.append(userid[temp[1]]+"님이 나갔습니다.")        
       
    print(answer)
    return answer
a=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(a)
