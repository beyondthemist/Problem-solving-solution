import sys
input = sys.__stdin__.readline

from typing import List, Dict, Set

def dfs(graph: Dict[int, List[int]], root: int, visited: Set[int]= set()):
    stack: List[int] = [root]
    stack_set = set(stack)
    while stack:
        v = stack.pop()
        stack_set.remove(v)

        if v not in visited:
            visited.add(v)
            
            for u in graph[v]:
                if u not in stack_set and u not in visited:
                    stack.append(u)
                    stack_set.add(u)
                
            graph[v] = []


n, m = [int(x) for x in input().split()]
graph: Dict[int, List[int]] = {}

for _ in range(m):
    u, v = [int(x) for x in input().split()]
    if u not in graph.keys():
        graph[u] = [v]
    else:
        graph[u].append(v)

    if v not in graph.keys():
        graph[v] = [u]
    else:
        graph[v].append(u)


count = n - len(graph.keys()) # nodes that have no edges
for v in graph.keys():
    if len(graph[v]) > 0:
        dfs(graph, v)
        count += 1
print(count)
