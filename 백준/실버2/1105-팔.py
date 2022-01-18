al,ar= input().split()

if len(al)!=len(ar):
    print(0)
else:
    pcount=0
    for i in range(len(al)):
        if al[i]==ar[i]:
            if al[i]=='8':
                pcount+=1
        # else:
        #     break
    print(pcount)