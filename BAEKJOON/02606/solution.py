import sys
input = sys.__stdin__.readline

def dfs(g, r=1, visited=[]):
    visited.append(r)

    for w in g[r]:
        if w not in visited:
            visited = dfs(g, w, visited=visited)

    return visited

n = int(input())
m = int(input())
g = {}
for _ in range(m):
    v, w = [int(x) for x in input().split()]
    if v not in g.keys():
        g[v] = [w]
    else:
        g[v].append(w)

    if w not in g.keys():
        g[w] = [v]
    else:
        g[w].append(v)

print(0 if m == 0 else len(dfs(g=g)) - 1)
