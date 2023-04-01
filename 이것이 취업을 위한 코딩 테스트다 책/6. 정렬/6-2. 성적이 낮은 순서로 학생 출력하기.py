## 입력값
# 2
# 홍길동 95
# 이순신 77   


n = int(input())
li = []
for i in range(n):
    data = input().split()
    li.append((data[0], int(data[1])))

li.sort(key=lambda data: data[1])

for i in li:
    print(i[0], end= ' ')