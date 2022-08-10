def solution(sizes):
    answer = 0
    aM, bM = 0, 0
    naM, nbM = 0, 0
    for i in sizes:
        if i[0]>aM:
            aM=i[0]
        if i[1]>bM:
            bM=i[1]
    
    if aM > bM:
        for i in sizes:
            if i[0]>=i[1] and i[1]>=nbM:
                nbM=i[1]
            elif i[0]<=i[1] and i[0]>=nbM:
                nbM=i[0]
        return aM*nbM                
    else:
        for i in sizes:
            if i[0]<=i[1] and i[0]>=naM:
                naM=i[0]
            elif i[0]>=i[1] and i[1]>=naM:
                naM=i[1]        
        return naM*bM
def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col
