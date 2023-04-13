number = list(input())
number.sort(reverse=True)

sum = 1
for val in number:
    val = int(val)
    if val==0:
        sum+=0
    else:
        if sum*val >=2000000000:
            sum+=val
        else:
            sum*=val
print(sum)    







