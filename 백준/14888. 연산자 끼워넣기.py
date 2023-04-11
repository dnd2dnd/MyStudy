n = int(input())
num = map(int, input().split())
op = map(int, input().split())

minV = 1101
maxV = -1

def sol(a):
    
    for i in range(4):
        if op[i]>0:
            if i==0:
                v+=a
            elif i==1:
                v-=1
            elif i==2:
                v*=1
            elif i==3:
                v//=1                                


