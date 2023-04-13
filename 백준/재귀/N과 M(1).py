n, m = map(int, input().split())

def sol(m, st=[]):
    if m==0:
        print(' '.join(map(str, st)))
        return 
    for i in range(1, n+1):
        print(i, m)
        if i not in st:            
            st.append(i)
            sol(m-1, st)
            st.pop()

sol(m)