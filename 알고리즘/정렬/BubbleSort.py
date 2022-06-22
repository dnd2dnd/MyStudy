arrayList=[2,5,4,7,3,6,1,8,9]

def Bubble_Sort(arr):
    k=len(arr)
    for k in range(len(arr),0,-1):
        for i in range(k-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(Bubble_Sort(arrayList))

