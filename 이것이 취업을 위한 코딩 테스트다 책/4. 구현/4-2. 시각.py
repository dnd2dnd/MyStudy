n = int(input())

# 0 ~ 60 = 3, 13, 23, 30, 31, 32, 33 34, 35, 36, 37, 38, 39, 43, 53


sum = 0
for i in range(n+1):
    if i==3 or i==13 or i==23:
        sum += (60*60)
    else:
        sum += (15*60+45*15)
print(sum)


## 답안
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count +=1
print(count)                