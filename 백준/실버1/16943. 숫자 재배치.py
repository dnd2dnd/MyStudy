A, B = list(input().split())

ctn = [0]*len(A)
A = list(A)
B = list(B)
A.sort()

for i in range(len(B)):
    if B[i] in A:
        ctn[i]=int(B[i])
        A.remove(B[i])

for i in ctn:
    if i!=0:
        ctn[i] = A.pop()

print(ctn)
        


