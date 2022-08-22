def solution(n, arr1, arr2):
    answer = []
    
    arr1L, arr2L = list(), list()
    
    for i in arr1:
        k = n-len(bin(i)[2:])
        arr1L.append("0"*k+bin(i)[2:])
        
    for i in arr2:
        k = n-len(bin(i)[2:])
        arr2L.append("0"*k+bin(i)[2:])        
    
    for i in range(n):
        block=""
        for k in range(n):
            if arr1L[i][k]=='0' and arr2L[i][k]=='0':
                block+=" "
            else:
                block+="#"
        answer.append(block)
    return answer