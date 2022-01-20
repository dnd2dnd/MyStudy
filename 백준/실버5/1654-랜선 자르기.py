import sys
k,n=map(int,input().split())
lan=[int(sys.stdin.readline()) for _ in range(k)]
ln,rn=1,max(lan)
print(lan)
# while ln<=rn:
#     sum=0
#     mid=(ln+rn)//2
#     for k in range(len(lan)):
#         sum+=lan[k]//mid
#     if sum>=n:
#         ln=mid+1
#     else:
#         rn=mid-1
# print(rn)