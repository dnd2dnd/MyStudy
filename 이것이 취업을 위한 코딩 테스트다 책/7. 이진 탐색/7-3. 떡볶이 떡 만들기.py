# 입력값
# 4 6
# 19 15 10 17

n, m = map(int, input().split())
datam = list(map(int, input().split()))
datam.sort()

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        sum = 0
        for ar in array:
            if ar<mid:
                continue
            sum += (ar-mid)
        if target < sum:
            start = mid + 1
        elif target > sum:
            end = mid - 1
        else:
            return mid
        
print(binary_search(datam, m, 0, max(datam)))


## 답안
n, m = map(int, input().split())
array = list(map(int, input().split))

start = 0 
end = max(array)

result = 0
while(start<=end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x>mid:
            total += x-mid
    if total < m:
        end = mid -1
    else:
        result = mid
        result = mid + 1
print(result)
