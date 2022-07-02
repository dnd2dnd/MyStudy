n = int(input())
numList = list(map(int, input().split()))
# for j in range(len(numList)):
#     for i in range(j,len(numList)):
#         sum=0
#         for k in range(j,i+1):
#             sum = sum + numList[k]
#             # print(k, sum, numList[k])105
#         if sum > max:
#             # print(max)
#             max = sum 

# sumList=list()
# print(max(numList))
# max=-1001
# sum=0

# for k in range(len(numList)):
#     sum = sum + numList[k]
#     if sum > max:
#         max = sum
#     sumList.append(sum)
# for k in range(len(numList)):
#     sumList.pop()

# print(max)

dp=[0]*len(numList)
dp[0]=numList[0]
for i in range(1,len(numList)):
    dp[i] = max(dp[i-1]+numList[i], numList[i])

print(max(dp))