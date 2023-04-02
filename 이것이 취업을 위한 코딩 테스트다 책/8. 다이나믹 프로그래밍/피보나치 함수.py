def fibo(x):
    if x==1 or x==2:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)
    
print(fibo(4))


d = [0] * 100

def fibo_recursion(x):
    if x==1 or x==2:
        return 1
    
    if d[x] != 0 :
        return d[x]
    
    d[x] = fibo_recursion(x-1) + fibo_recursion(x-2)
    return d[x]

print(fibo_recursion(99))