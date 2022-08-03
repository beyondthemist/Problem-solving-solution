n = int(input())
a = [-1] + [int(x) for x in input().split()]
d = [([1 for col in range(n + 1)] + [0]) for row in range(n + 1)]

for j in range(n, 0, -1):
    for i in range(j):
        d[i][j] = d[i][j + 1] if a[i] >= a[j] else max(d[i][j + 1], 1 + d[j][j + 1])

print(d[0][1])
