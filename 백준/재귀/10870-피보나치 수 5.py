n = int(input())

def fac(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fac(n-1) + fac(n-2)
    
print(fac(n))
