# https://www.acmicpc.net/problem/9184

n = 21
d = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            if a <= 0 or b <= 0 or c <= 0:
                d[a][b][c] = 1
            elif a < b and b < c:
                d[a][b][c] = d[a][b][c - 1] + d[a][b - 1][c - 1] - d[a][b - 1][c]
            else:
                d[a][b][c] = d[a - 1][b][c] + d[a - 1][b - 1][c] + d[a - 1][b][c - 1] - d[a - 1][b - 1][c - 1]

a, b, c = [int(x) for x in input().split()]
while not (a == -1 and b == -1 and c == -1):
    if a <= 0 or b <= 0 or c <= 0:
        print(f'w({a}, {b}, {c}) = {d[0][0][0]}')
    elif a > 20 or b > 20 or c > 20:
        print(f'w({a}, {b}, {c}) = {d[20][20][20]}')
    else:
        print(f'w({a}, {b}, {c}) = {d[a][b][c]}')
    a, b, c = [int(x) for x in input().split()]
