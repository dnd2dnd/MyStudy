li=[]
n=0
for i in range(0, 5):
    ip=int(input())
    n+=ip
    li.append(ip)
li.sort()
print(n//5)
print(li[2])

