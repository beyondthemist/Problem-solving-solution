import sys
input = sys.__stdin__.readline

def prefix_sum(a, x1, y1, x2, y2):
    return a[x2][y2] - a[x2][y1 - 1] - a[x1 - 1][y2] + a[x1 - 1][y1 - 1]

def solution():
    n, m = [int(x) for x in input().split()]

    a = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        a.append([0] + [int(x) for x in input().split()])

    for i in range(n + 1):
        for j in range(1, n + 1):
            a[i][j] += a[i][j - 1]
    for j in range(n + 1):
        for i in range(1, n + 1):
            a[i][j] += a[i - 1][j]

    for _ in range(m):
        x1, y1, x2, y2 = [int(x) for x in input().split()]
        print(prefix_sum(a, x1, y1, x2, y2))

solution()
