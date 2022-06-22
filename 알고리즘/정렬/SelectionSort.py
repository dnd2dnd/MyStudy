arrayList=[2,5,4,7,3,6,1,8,9]

def selection_sort(arrayList):
    for i in range(len(arrayList)-1):
        indexV = arrayList.index(min(arrayList[i:]))
        arrayList[i], arrayList[indexV] = arrayList[indexV], arrayList[i]
    print(arrayList)

def selection_sort_Internet_Code(arrayList):
    for i in range(len(arrayList)-1):
        min_index = i 
        for k in range(i+1, len(arrayList)):
            if arrayList[k] < arrayList[min_index]:
                min_index = k
        arrayList[i], arrayList[min_index] = arrayList[min_index], arrayList[i]
    return arrayList;    
selection_sort(arrayList)    
print(selection_sort_Internet_Code(arrayList))
