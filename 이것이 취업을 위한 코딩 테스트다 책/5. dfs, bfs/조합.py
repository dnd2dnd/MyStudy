n, m = map(int, input().split())

data_A = []
data_B = []

def dfs_A(i, list):
    if len(list)==m:
        data_A.append(list)
        return
    
    for i in range(i, n):
        dfs_A(i+1, list+[i+1])

def dfs_B(i, list):
    if len(list)==m:
        data_B.append(list)
        return
    
    for i in range(i, n):
        dfs_B(i, list+[i+1])        


dfs_A(0, [])
dfs_B(0, [])

print(data_A)
print(data_B)