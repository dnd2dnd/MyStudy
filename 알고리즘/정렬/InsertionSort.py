arrayList=[2,5,4,7,3,6,1,8,9]

def Insertion_sort(arr):
    for i in range(1,len(arr)):
        is_index = i
        for k in range(i-1,-1,-1):
            if arr[k] > arr[is_index]:
                arr[k], arr[is_index] = arr[is_index], arr[k]
                is_index=k
            else:
                break
    return arr

def Insertion_sort_Internet_Code(arr):
    for end in range(1, len(arr)):
        for i in range(end,0,-1):
            if(arr[i-1] > arr[i]):
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr
print(Insertion_sort(arrayList))
print(Insertion_sort_Internet_Code(arrayList))