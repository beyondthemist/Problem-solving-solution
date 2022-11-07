import sys 
input = sys.stdin.readline

def bfs(n: int, k: int):
    if n >= k:
        return n - k

    graph = [0 for _ in range(2*k)]
    visited = set()
    q = [n]

    while q:
        curr = q.pop(0)

        if curr == k:
            return graph[curr]

        visited.add(curr)
        for next in set([curr - 1, curr + 1, 2*curr]) - visited:
            if (next not in visited) and (0 <= next < 2*k):
                q.append(next)
                visited.add(next)
                if graph[next] <= 0:
                    graph[next] = graph[curr] + 1
                else:
                    graph[next] = min(graph[next], graph[curr] + 1)
                

n, k = [int(x) for x in input().split()]
print(bfs(n=n, k=k))
