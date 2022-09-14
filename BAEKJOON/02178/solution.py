n, m = [int(x) for x in input().split()]
grid = [[int(c) for c in input()] for _ in range(n)]
q = [(0, 0)]

while q:
    v = q.pop(0)
    i, j = v[0], v[1]
    di_list = [0, 0, -1, 1]
    dj_list = [-1, 1, 0, 0]

    for di, dj in zip(di_list, dj_list):
        x, y = (i + di), j + dj

        if (0 <= x and x < n) \
        and (0 <= y and y < m) \
        and grid[x][y] == 1:
            q.append((x, y))
            grid[x][y] += grid[i][j]

print(grid[n - 1][m - 1])
