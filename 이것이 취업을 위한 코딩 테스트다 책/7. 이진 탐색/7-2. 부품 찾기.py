# 입력값
# 5
# 8 3 7 9 2
# 3 
# 5 7 9

n = int(input())
ndata = list(map(int, input().split()))
m = int(input())
mdata = map(int, input().split())

# 정렬 활용안한 풀이
# for md in mdata:
#     if md in ndata:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')


ndata.sort()
def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            print("yes", end=' ')
            return None
    print("no", end=' ')
    return None

for md in mdata:
    binary_search(ndata, md, 0, n-1)

