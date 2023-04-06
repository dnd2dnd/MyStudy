
def numberlig(s, list):
    if len(list)==n:
        data.append(list)
        return 
    for i in range(s, k):
        numberlig(i+1, list+[num[i]])

while True:
    num = list(map(int, input().split()))
    data = []
    k = num[0]
    num.remove(k)
    n=6
    if k==0:
        break
    
    numberlig(0, [])
    for d in data:
        print(*d)
    
    print("")






