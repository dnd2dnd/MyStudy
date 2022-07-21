# 인터넷에서 참고한 코드
from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)
    stopId = []
    for i in report:
        a, b = i.split(" ")
        user[a].add(b)
        cnt[b]+=1
    for i in id_list:
        result=0
        for j in user[i]:
            if cnt[j] >= k:
                result+=1
        answer.append(result)
    return answer

# 나의 풀이
# 테스트는 통과했지만 조건에 정확성 테스트로 시간 제한이 있었기 때문에 실패한 코드
# 
# def solution(id_list, report, n):
#     answer = [0]*len(id_list)
#     reportId = [[0]*1 for i in range(len(id_list))]
#     countId = [0]*(len(id_list))
#     stopId = []
#     for i in range(len(report)):
#         text=report[i].split(" ")
#         for k in range(len(id_list)):
#             if text[0]==id_list[k] and text[1] not in reportId[k]:
#                 reportId[k].append(text[1])
#                 break
#     reId = sum(reportId, [])
#     for i in range(len(reId)):
#         for k in range(len(id_list)):
#             if reId[i]==0:
#                 break
#             if reId[i]==id_list[k]:
#                 countId[k]+=1
#     for i in range(len(countId)):
#         if countId[i] >=n:
#             stopId.append(id_list[i])
#     for i in range(len(reportId)):
#         for k in range(1,len(reportId[i])):
#             if reportId[i][k] in stopId:
#                 answer[i]+=1
#     return answer