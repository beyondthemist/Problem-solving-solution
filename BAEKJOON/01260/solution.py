def dfs(graph, v, visited=[]):
    visited.append(v)
    if v in graph.keys() or v in graph.values():
        for w in graph[v]:
            if w not in visited:
                visited = dfs(graph, w, visited)
    
    return visited

def bfs(graph, v):
    visited = [v, ]
    queue = [v, ]
    if v in graph.keys() or v in graph.values():
        while queue:
            t = queue.pop(0)
            for w in graph[t]:
                if w not in visited:
                    visited.append(w)
                    queue.append(w)
    
    return visited

n, m, v = [int(x) for x in input().split()]
graph = {}
for _ in range(m):
    v1, v2 = [int(x) for x in input().split()]
    if v1 not in graph.keys():
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)

    if v2 not in graph.keys():
        graph[v2] = [v1]
    else:
        graph[v2].append(v1)

for key in graph.keys():
    graph[key].sort()

print(' '.join([str(x) for x in dfs(graph, v)]))
print(' '.join([str(x) for x in bfs(graph, v)]))
