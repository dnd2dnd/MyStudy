s = list(input())
alp=[]
sum=0
for val in s:
    if val.isdigit():
        sum+=int(val)
    else:
        alp.append(val)

alp.sort()
for i in alp:
    print(i, end='')
print(sum,end='')