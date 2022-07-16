n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

sorted_data = sorted(data)
for i in range(n):
    print(sorted_data[i])