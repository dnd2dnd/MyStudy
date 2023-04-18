import sys
input = sys.stdin.readline

n = int(input())
perm = list(map(int, input().split()))

# 맨 뒤부터 탐색
for i in range(n-1, 0, -1):
    # 뒷 값이 앞 값보다 크면
    if perm[i-1] < perm[i]:
        # 다시 뒤에서부터, 앞 값보다 큰 값이 있는지 탐색
        for j in range(n-1, 0, -1):
            # 뒷 값이 앞 값보다 크면
            if perm[i-1] < perm[j]:
                # 두 값을 swap
                perm[i-1], perm[j] = perm[j], perm[i-1]
                # 뒷 값의 인덱스부터 끝까지 오름차순 정렬 후 출력
                perm = perm[:i] + sorted(perm[i:])
                print(" ".join(map(str, perm)))
                exit()
# 만약 뒷 값이 앞 값보다 큰 경우가 없다면, 맨 마지막 순열이므로 -1
print(-1)

#     cnt=0
#     for k in range(n):
#         if numbers[i][k]==m[k]:
#             cnt+=1
#         else:
#             break
    
#     if cnt==n:
#         check=1
#         if i==len(numbers)-1:
#             print(-1)

