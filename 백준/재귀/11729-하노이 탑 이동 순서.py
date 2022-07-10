from tabnanny import check


k = int(input())

al=list()
def fac(k,a,c,b,al):
    if k == 1:
        al.append([a,c])
    else:
        fac(k-1,a,b,c,al)
        al.append([a,c])
        fac(k-1,b,c,a,al)
    
    

fac(k,1,3,2, al)
print(len(al))
for i in range(len(al)):
    print(al[i][0], al[i][1])
