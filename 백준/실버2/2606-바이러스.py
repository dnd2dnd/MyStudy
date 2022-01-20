cn=int(input()) # 컴퓨터 수
nn=int(input()) # 네트워크 수
computer=[[] for _ in range(cn+1)]

for i in range(nn):
    a,b=map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)

# def dfs(computer,start_node,visited=[]):
#     visited.append(start_node)
    
#     for node in computer[start_node]:
#         if node not in visited:
#             dfs(computer,node,visited)
#     return len(visited)-1

# print(dfs(computer,1))

def bfs(computer,start_node):
    need_visited, visited = list(), list()

    need_visited.append(start_node)
    while need_visited:
        node=need_visited[0]
        del need_visited[0]
        if node not in visited:
            visited.append(node)
            need_visited.extend(computer[node])
    return visited

print(bfs(computer,1))