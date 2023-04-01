## 입력값
# 10 7
# 1 3 5 7 9 11 13 15 17 19
# 4

# 이진 탐색 - 배열 내부의 데이터가 이미 정렬되어 있어야함
def binary_seach(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_seach(array, target, start, mid - 1)
    else:
        return binary_seach(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_seach(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)