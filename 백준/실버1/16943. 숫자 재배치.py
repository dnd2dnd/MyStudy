from itertools import permutations

a, b = input().split()
b = int(b)
c = -1

a_list = []
for item in permutations(a):
    a_list.append(''.join(item))

for i in a_list:
    if i[0] == '0':  # 0으로 시작하는 경우
        continue
    i = int(i)
    if i < b:
        c = max(c, i)

print(c)