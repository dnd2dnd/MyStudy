n = int(input())
li = list()

while n>0:
    li.append(n%10)
    n = n//10
li.sort()

ans=0
for i in range(len(li)):
    ans+=li[i]*10**i
print(ans)