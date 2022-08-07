def bfs(grid, i, j, n, m):
    if grid[i][j] != 1:
        return

    q = [(i, j)]
    visited = []
    while q:
        v = q.pop(0)
        if v not in visited and grid[v[0]][v[1]] == 1:
            visited.append(v)
            grid[v[0]][v[1]] = 0

            q.append((max(v[0] - 1, 0), v[1]))
            q.append((min(v[0] + 1, n - 1), v[1]))
            q.append((v[0], max(v[1] - 1, 0)))
            q.append((v[0], min(v[1] + 1, m - 1)))
                    

t = int(input())
for x in range(t):
    m, n, k = list(map(int, input().split()))
    acre = [[0 for col in range(m)] for row in range(n)]

    for y in range(k):
        j, i = list(map(int, input().split()))
        acre[i][j] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if acre[i][j] == 1:
                bfs(acre, i, j, n, m)
                count += 1
    print(count)
