n=int(input())
numArray=list()
while(n>0):
    k=int(input())
    numArray.append(k)
    for i in range(len(numArray)-1):
        if numArray[i]>k:
            numArray[i],numArray[len(numArray)-1] = numArray[len(numArray)-1], numArray[i]
    n=n-1

for k in range(len(numArray)):
    print(numArray[k])
