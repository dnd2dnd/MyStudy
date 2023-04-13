n = int(input())

member = list(map(int, input().split()))
member.sort()

count = 0 
group = []

for i in range(n):
    s = member.pop(0)
    group.append(s)

    if max(group) == len(group):
        count +=1
        group = []

print(count)


## 답안
# 입력
N = int(input())
people = list(map(int, input().split()))

# 길드원 공포도 오름차순 정렬
people.sort()

# 결과값 및 인원수 측정 객체 초기화
result = 0    # 그룹수
count = 0     # 그룹의 인원수

# 메인
for panic in people:
    count += 1 # 그룹인원 추가
    if count >= panic: # 인원의 공포도가 그룹의 인원수보다 적으면,
        result += 1    # 그룹을 형성한다. 
        count = 0      # 인원수를 다시 초기화 한다. 
        
print(result)
    





    



