import sys
n = int(input())
arr = [0] * 10000

for i in range(n):
    a = int(sys.stdin.readline())
    arr[a-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
