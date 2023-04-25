import math
N = int(input())
li = list(map(int, input().split()))
order = li.pop(0)

def sol(n, k):
    if len(answer) == N-1:
        answer.append(numbers[-1])
        return
    
    mf = math.factorial(n-1)
    value = math.ceil(k/mf)
    answer.append(numbers.pop(value))

    sol(n-1, k - (mf*(value-1)))
    
def sol_2():
    global answer
    n = N
    for i in li:
        mf = math.factorial(n-1)
        answer += (numbers.index(i) * mf)
        numbers.remove(i)
        n-=1


if order == 1:
    numbers = [x for x in range(N+1)]
    answer = []
    sol(N, li[0])
    print(' '.join(list(map(str, answer))))
elif order == 2:
    numbers = [x for x in range(1, N+1)]
    answer=0
    sol_2()
    print(answer+1)