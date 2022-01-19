n,m,v=map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

def dfs(graph, start_node, visited=[]):
    dfs_str=''
    visited.append(start_node)
    for node in graph[start_node]:
        if node not in visited:
            dfs(graph, node, visited)

    for i in visited:
        dfs_str+=str(i)+' '
    return dfs_str
def bfs(graph, start_node):
    bfs_str=''    
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    for i in visited:
        bfs_str+=str(i)+' '
    return bfs_str


print(dfs(graph, v))
print(bfs(graph, v))
